from pyspark.sql import DataFrame
from pyspark.sql.functions import col, avg, count

def compute_user_features(df: DataFrame):
    return df.groupBy("user_id").agg(
        count("transaction_id").alias("txn_count"),
        avg("amount").alias("avg_amount")
    )

def compute_device_features(df: DataFrame):
    return df.groupBy("device_id").agg(
        count("transaction_id").alias("device_txn_count"),
        avg("amount").alias("device_avg_amount")
    )
