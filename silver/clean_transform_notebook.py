# Databricks notebook content converted to Python
from pyspark.sql import SparkSession
from transformation_utils import deduplicate, normalize_currency, enrich_metadata

spark = SparkSession.builder.appName("SilverTransform").getOrCreate()

bronze_path = "abfss://<container>@<account>.dfs.core.windows.net/bronze/"
silver_path = "abfss://<container>@<account>.dfs.core.windows.net/silver/"

df = spark.read.format("delta").load(bronze_path)

df = deduplicate(df, subset=["transaction_id"])
df = normalize_currency(df)
df = enrich_metadata(df)

df.write.format("delta").mode("overwrite").save(silver_path)
