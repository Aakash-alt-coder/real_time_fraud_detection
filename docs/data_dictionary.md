
---

## **`data_dictionary.md`**
```markdown
# Data Dictionary - Real-Time Fraud Detection

## 1. Transaction Event Schema (Streaming & Bronze Layer)
| Field Name       | Type    | Description                                  |
|-----------------|--------|----------------------------------------------|
| user_id          | string | Unique identifier for the user               |
| transaction_id   | string | Unique identifier for the transaction       |
| amount           | double | Transaction amount                           |
| currency         | string | Transaction currency (USD, EUR, etc.)       |
| merchant_id      | string | Unique identifier for the merchant          |
| timestamp        | string | ISO timestamp of the transaction            |
| location         | string | City or region of the transaction           |
| device_type      | string | Type of device (mobile, desktop, tablet)   |
| device_id        | string | Unique identifier of the device             |
| payment_method   | string | Method used for payment (card, PayPal, etc.)|

---

## 2. Silver Layer Enriched Fields
| Field Name       | Type    | Description                                  |
|-----------------|--------|----------------------------------------------|
| risk_score       | double | Placeholder for computed fraud risk score    |
| normalized_currency | string | Lowercase standardized currency value      |
| metadata         | struct | Additional enriched metadata (location, device info, etc.) |

---

## 3. Gold Layer / Aggregates
| Field Name       | Type    | Description                                  |
|-----------------|--------|----------------------------------------------|
| total_transactions | integer | Total transactions per aggregation          |
| total_amount       | double | Sum of transaction amounts                   |
| high_risk_count    | integer | Count of transactions with high risk        |
| top_risk_users     | string  | User IDs with highest risk scores            |

---

## 4. Feature Store

### **User Features**
| Feature Name     | Type    | Description                                  |
|-----------------|--------|----------------------------------------------|
| txn_count        | integer | Total transactions for the user             |
| avg_amount       | double  | Average transaction amount                   |
| last_txn_time    | string | Timestamp of last transaction               |
| high_risk_count  | integer | Number of high-risk transactions            |

### **Device Features**
| Feature Name     | Type    | Description                                  |
|-----------------|--------|----------------------------------------------|
| device_txn_count | integer | Total transactions from the device          |
| device_avg_amount| double  | Average transaction amount on device        |
| device_risk_score| double  | Computed device risk score                  |

---

## Notes
- All layers are stored in **Delta format** in ADLS Gen2.
- Feature tables are updated incrementally for real-time scoring.
- Sensitive fields (PII) are masked before storing in Gold layer.
