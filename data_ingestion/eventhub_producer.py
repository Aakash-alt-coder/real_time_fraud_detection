import json
import time
import random
from datetime import datetime
from faker import Faker
from azure.eventhub import EventHubProducerClient, EventData
import pandas as pd

# Load Event Hub config
import json
with open("config.json") as f:
    config = json.load(f)

producer = EventHubProducerClient(
    fully_qualified_namespace=config['event_hub_namespace'],
    eventhub_name=config['event_hub_name'],
    credential=config['sas_key']
)

fake = Faker()

CURRENCIES = ['USD', 'EUR', 'GBP', 'INR']
DEVICES = ['mobile', 'desktop', 'tablet']
PAYMENT_METHODS = ['credit_card', 'debit_card', 'paypal', 'netbanking']

def generate_transaction():
    return {
        "user_id": fake.uuid4(),
        "transaction_id": fake.uuid4(),
        "amount": round(random.uniform(10, 5000), 2),
        "currency": random.choice(CURRENCIES),
        "merchant_id": fake.uuid4(),
        "timestamp": datetime.utcnow().isoformat(),
        "location": fake.city(),
        "device_type": random.choice(DEVICES),
        "device_id": fake.uuid4(),
        "payment_method": random.choice(PAYMENT_METHODS)
    }

def send_events(batch_size=10, interval=1):
    while True:
        batch = []
        for _ in range(batch_size):
            batch.append(EventData(json.dumps(generate_transaction())))
        with producer:
            producer.send_batch(batch)
        print(f"Sent {batch_size} events")
        time.sleep(interval)

if __name__ == "__main__":
    send_events(batch_size=20, interval=2)
