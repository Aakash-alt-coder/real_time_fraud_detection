## Features
- Real-time streaming ingestion using Azure Event Hub
- Lakehouse architecture (Bronze/Silver/Gold) in ADLS Gen2
- Real-time fraud scoring with ML models
- Feature store for user/device risk features
- Power BI dashboards for analytics
- Orchestrated batch & streaming pipelines via ADF/Airflow
- Monitoring, alerting, and data quality checks

## Setup Instructions
1. Clone the repo.
2. Install Python dependencies: `pip install -r data_ingestion/requirements.txt`
3. Configure Azure Event Hub in `data_ingestion/config.json`
4. Start Event Hub producer: `python data_ingestion/eventhub_producer.py`
5. Run ingestion scripts in `bronze/`
6. Run transformations in Databricks notebooks (`silver/` & `gold/`)
7. Access dashboards in Power BI

## Folder Structure
<Insert full folder structure here>

## Architecture Diagram
For the detailed architecture diagram, see [ARCHITECTURE.md](docs/ARCHITECTURE.md)
