# Project Architecture

## System Design

The system is designed to monitor and analyze the energy consumption of IT infrastructure using Prometheus for data collection and Grafana for data visualization.
The architecture mirrors the following schematic:

```mermaid
graph TD
        %% Park of machines
        subgraph Park_of_Machines["Park of Machines"]
            direction TB
            subgraph Main Machine["Main Machine with Prometheus"]
                M1[Machine 1]
                E1[Node Exporter 1]
                PH[Prometheus Hook]

            end
            M2[Machine 2]
            M3[Machine 3]
            M4[Machine 4]
    
            E2[Node Exporter 2]
            E3[Node Exporter 3]
            E4[Node Exporter 4]

            M1 --> E1
            M2 --> E2
            M3 --> E3
            M4 --> E4

            E1 --> PH
            E2 --> PH
            E3 --> PH
            E4 --> PH
        end


        %% Grafana and visualization
        subgraph GrafanaStack["Grafana"]
            G[Grafana]
            Dash[Dashboards]
            G --> Dash
        end

        %% Dashboard Analysis
        subgraph Visualization["Visualization & Analysis"]
        ECA[Data Decriptions]
        DA[Data Analysis]
        ECA --> DA
        end

        A[Alerting]
        R[Recommendations]
        D[Dashboards]

        %% Connections

        PH --> G
        Dash -->|Grafana API| ECA
        DA --> A
        DA --> R
        DA --> D
    
```
