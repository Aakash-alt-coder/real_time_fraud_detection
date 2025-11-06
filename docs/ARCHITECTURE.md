# Real-Time Fraud Detection & Analytics Platform - Architecture

## Overview
This project implements a **real-time fraud detection platform** using Azure Cloud services and a Lakehouse architecture. It supports streaming ingestion, batch processing, real-time ML scoring, feature storage, and dashboard reporting.

---

## **Architecture Components**

### 1. Streaming Data Ingestion
- **Azure Event Hub** receives financial transactions in real-time.
- Python **EventHubProducer** generates synthetic transactions.
- Event schema includes: `user_id, transaction_id, amount, currency, merchant_id, timestamp, location, device_type, device_id, payment_method`.

### 2. Bronze Layer (Raw Data)
- **ADLS Gen2** stores raw events as **Delta/Parquet**.
- Append-only storage for traceability.
- Schema validation applied using `schema.json`.

### 3. Silver Layer (Cleaned & Enriched)
- Databricks notebooks perform:
    - Deduplication
    - Field normalization (currency, device type)
    - Metadata enrichment (risk placeholders, location metadata)
- Delta tables used for incremental updates.

### 4. Gold Layer (Aggregations & Fraud Scoring)
- ML models (Isolation Forest / XGBoost / Logistic Regression) score transactions in **real-time**.
- High-risk transactions trigger **alerts** via Email/Slack/Teams.
- Aggregated metrics stored in Delta tables for dashboards.

### 5. Feature Store
- User-level and device-level features stored in Delta tables.
- Examples:
    - `user_features`: transaction count, average amount, last transaction time
    - `device_features`: device risk score, transaction volume

### 6. Orchestration
- **Azure Data Factory (ADF)** pipelines or **Airflow DAGs** manage batch and streaming workflows.
- Includes dependency management, scheduling, retries, and error handling.

### 7. Monitoring & Observability
- **Great Expectations** for data quality checks.
- **Azure Monitor / Log Analytics** for pipeline health and metrics.
- Alerts on failures or high-risk transactions.

### 8. Dashboard & Reporting
- **Power BI** dashboards display:
    - Total transactions & amounts
    - Fraudulent/high-risk transactions
    - Transaction trends by region, device, or merchant
    - Top high-risk users

---

## **Pipeline Flow Diagram**

```text
[Event Hub Producer] --> [Azure Event Hub] --> [Bronze Delta Layer] --> [Silver Transformations] --> [Gold Fraud Scoring & Aggregates] --> [Feature Store] --> [Power BI Dashboard]
                                                |                                        |
                                                +--> [Data Quality / Monitoring]        +--> [Alert System]
