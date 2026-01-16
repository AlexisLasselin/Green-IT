import requests
from prometheus_client import Gauge, start_http_server
import time
from collections import deque
from datetime import datetime, timezone, timedelta

# ===========================
# CONFIGURATION
# ===========================
PROM_URL = "http://192.168.228.128:9090"  # Prometheus VM
JOB_NAME = "node_vm"
EXPORTER_PORT = 8000
NUM_CORES = 10
POWER_CPU_W = 15
POWER_RAM_W = 2
POWER_DISK_W = 5
POWER_NET_W = 1
CO2_PER_KWH = 6          # gCO2/kWh EDF 2024
SLEEP_INTERVAL = 30      # secondes

# ===========================
# METRICS PROMETHEUS EXPORT
# ===========================
instant_metric = Gauge(
    "carbon_emission_instant_grams",
    "Estimated CO2 emissions per VM at current instant",
    ["instance_name"]
)

cumul_metric = Gauge(
    "carbon_emission_cumul_grams",
    "Estimated CO2 emissions per VM over the last hour",
    ["instance_name"]
)

instant_total_metric = Gauge(
    "carbon_emission_instant_total_grams",
    "Estimated CO2 emissions for the whole VM park at current instant"
)

cumul_total_metric = Gauge(
    "carbon_emission_cumul_total_grams",
    "Estimated CO2 emissions for the whole VM park over the last hour"
)

start_http_server(EXPORTER_PORT)
print(f"Prometheus metrics exposed on port {EXPORTER_PORT}")

# ===========================
# HISTORIQUE POUR CUMUL 1H
# ===========================
# {instance_name: deque of (timestamp, co2_instant)}
history = {}

# ===========================
# FONCTION UTILE
# ===========================
def get_prometheus_metric(query):
    try:
        response = requests.get(f"{PROM_URL}/api/v1/query", params={"query": query})
        data = response.json()
        result = data.get("data", {}).get("result", [])
        if not result:
            return 0.0
        return float(result[0]["value"][1])
    except Exception as e:
        print("Erreur API Prometheus:", e)
        return 0.0

def get_active_instances():
    response = requests.get(f"{PROM_URL}/api/v1/series", params={"match[]": f'up{{job="{JOB_NAME}"}}'})
    data = response.json().get("data", [])
    instances = []
    for item in data:
        instance_name = item.get("instance_name")
        instance_addr = item.get("instance")
        if not instance_name:
            instance_name = instance_addr
        if get_prometheus_metric(f'up{{job="{JOB_NAME}", instance="{instance_addr}"}}') == 1:
            instances.append((instance_addr, instance_name))
    return instances

# ===========================
# BOUCLE PRINCIPALE
# ===========================
while True:
    active_instances = get_active_instances()
    if not active_instances:
        print("Aucune VM active, attente 10s...")
        time.sleep(10)
        continue

    now = datetime.now(timezone.utc)
    total_instant = 0.0
    total_cumul = 0.0

    for instance_addr, instance_name in active_instances:
        # --- CPU ---
        cpu_usage = min(get_prometheus_metric(
            f'rate(node_cpu_seconds_total{{job="{JOB_NAME}", instance="{instance_addr}", mode!="idle"}}[5m])'
        ), 1.0)
        energy_cpu_kwh = cpu_usage * NUM_CORES * POWER_CPU_W * SLEEP_INTERVAL / 3600 / 1000  # kWh sur 30s

        # --- RAM ---
        mem_total_gb = get_prometheus_metric(f'node_memory_MemTotal_bytes{{job="{JOB_NAME}", instance="{instance_addr}"}}') / (1024**3)
        mem_avail_gb = get_prometheus_metric(f'node_memory_MemAvailable_bytes{{job="{JOB_NAME}", instance="{instance_addr}"}}') / (1024**3)
        ram_used_gb = mem_total_gb - mem_avail_gb
        energy_ram_kwh = ram_used_gb * POWER_RAM_W * SLEEP_INTERVAL / 3600 / 1000

        # --- Disk ---
        disk_io = get_prometheus_metric(f'node_disk_io_time_seconds_total{{job="{JOB_NAME}", instance="{instance_addr}"}}')
        energy_disk_kwh = disk_io * POWER_DISK_W * SLEEP_INTERVAL / 3600 / 1000

        # --- Network ---
        net_bytes = get_prometheus_metric(f'node_network_receive_bytes_total{{job="{JOB_NAME}", instance="{instance_addr}"}}')
        energy_net_kwh = (net_bytes / 1e9) * POWER_NET_W * SLEEP_INTERVAL / 3600 / 1000

        # --- Instant CO2 ---
        co2_instant = (energy_cpu_kwh + energy_ram_kwh + energy_disk_kwh + energy_net_kwh) * CO2_PER_KWH
        instant_metric.labels(instance_name=instance_name).set(co2_instant)
        total_instant += co2_instant

        # --- Historique pour cumul ---
        if instance_name not in history:
            history[instance_name] = deque()
        history[instance_name].append((now, co2_instant))

        # Nettoyer l'historique > 1h
        while history[instance_name] and history[instance_name][0][0] < now - timedelta(hours=1):
            history[instance_name].popleft()

        # --- Cumul 1h ---
        co2_cumul = sum([x[1] for x in history[instance_name]])
        cumul_metric.labels(instance_name=instance_name).set(co2_cumul)
        total_cumul += co2_cumul

        print(f"{instance_name} ({instance_addr}) - Instant CO2: {co2_instant:.3f} g | Last hour CO2: {co2_cumul:.3f} g")

    # --- CO2 total parc ---
    instant_total_metric.set(total_instant)
    cumul_total_metric.set(total_cumul)
    print(f"Total parc - Instant CO2: {total_instant:.3f} g | Last hour CO2: {total_cumul:.3f} g")

    print("================================================================================================")

    time.sleep(SLEEP_INTERVAL)
