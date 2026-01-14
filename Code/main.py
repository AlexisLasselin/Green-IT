import requests
from prometheus_client import Gauge, start_http_server
import time

# ===== CONFIG =====
PROM_URL = "http://192.168.228.128:9090"
NODE_JOB = "node_vm"
INSTANCE_NAME = "Main"

NUM_CORES = 4        
POWER_CPU_W = 60     
POWER_RAM_W = 2      
CO2_PER_KWH = 50     # gCO₂/kWh
DURATION_HOURS = 1 

# ===== METRICS PROMETHEUS EXPORT =====
co2_metric = Gauge("carbon_emission_grams", "Estimated CO2 emissions per VM", ["instance"])
start_http_server(8000)

# ===== FONCTIONS =====
def get_prometheus_metric(query):
    response = requests.get(f"{PROM_URL}/api/v1/query", params={"query": query})
    data = response.json()
    try:
        value = float(data["data"]["result"][0]["value"][1])
    except (IndexError, KeyError):
        value = 0.0
    return value

# ===== MAIN LOOP =====
while True:
    # CPU
    cpu_usage = get_prometheus_metric(
        f'rate(node_cpu_seconds_total{{job="{NODE_JOB}", mode!="idle"}}[5m])'
    )
    energy_cpu_kwh = cpu_usage * NUM_CORES * POWER_CPU_W * DURATION_HOURS / 1000

    # RAM
    mem_total_gb = get_prometheus_metric(f'node_memory_MemTotal_bytes{{job="{NODE_JOB}"}}') / (1024**3)
    mem_available_gb = get_prometheus_metric(f'node_memory_MemAvailable_bytes{{job="{NODE_JOB}"}}') / (1024**3)
    ram_used_gb = mem_total_gb - mem_available_gb
    energy_ram_kwh = ram_used_gb * POWER_RAM_W * DURATION_HOURS / 1000

    # Total CO2
    total_energy_kwh = energy_cpu_kwh + energy_ram_kwh
    total_co2 = total_energy_kwh * CO2_PER_KWH

    # Expose metric
    co2_metric.labels(instance=INSTANCE_NAME).set(total_co2)

    print(f"Estimated CO₂ for {INSTANCE_NAME}: {total_co2:.5f} g")

    time.sleep(10)
