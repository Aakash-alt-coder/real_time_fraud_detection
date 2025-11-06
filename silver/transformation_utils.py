from pyspark.sql import DataFrame
from pyspark.sql.functions import col, lower

def deduplicate(df: DataFrame, subset: list):
    return df.dropDuplicates(subset=subset)

def normalize_currency(df: DataFrame):
    return df.withColumn("currency", lower(col("currency")))

def enrich_metadata(df: DataFrame):
    # Example: Add risk score placeholder
    return df.withColumn("risk_score", col("amount") * 0.0)
