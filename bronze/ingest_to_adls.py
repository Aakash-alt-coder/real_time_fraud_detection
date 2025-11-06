from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, DoubleType
import json

# Load schema
with open("schema.json") as f:
    schema_json = json.load(f)

fields = [StructField(f['name'], StringType() if f['type']=='string' else DoubleType(), True)
          for f in schema_json['fields']]
schema = StructType(fields)

spark = SparkSession.builder.appName("BronzeIngestion").getOrCreate()

# Read streaming data from Event Hub
connectionString = "<EVENT_HUB_CONNECTION_STRING>"

df = spark.readStream.format("eventhubs").option("connectionString", connectionString).load()

# Convert body to string and parse JSON
from pyspark.sql.functions import col, from_json
df = df.withColumn("body_str", col("body").cast("string"))
df_parsed = df.withColumn("data", from_json(col("body_str"), schema)).select("data.*")

# Write to ADLS Gen2 in Delta format
df_parsed.writeStream.format("delta") \
    .option("checkpointLocation", "abfss://<container>@<account>.dfs.core.windows.net/checkpoints/bronze/") \
    .outputMode("append") \
    .start("abfss://<container>@<account>.dfs.core.windows.net/bronze/")
