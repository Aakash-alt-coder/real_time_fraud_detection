from pyspark.sql import SparkSession
from feature_utils import compute_device_features

spark = SparkSession.builder.appName("DeviceFeatures").getOrCreate()
silver_path = "abfss://<container>@<account>.dfs.core.windows.net/silver/"
feature_path = "abfss://<container>@<account>.dfs.core.windows.net/feature_store/device_features/"

df = spark.read.format("delta").load(silver_path)
device_features = compute_device_features(df)
device_features.write.format("delta").mode("overwrite").save(feature_path)
