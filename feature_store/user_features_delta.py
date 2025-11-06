from pyspark.sql import SparkSession
from feature_utils import compute_user_features

spark = SparkSession.builder.appName("UserFeatures").getOrCreate()
silver_path = "abfss://<container>@<account>.dfs.core.windows.net/silver/"
feature_path = "abfss://<container>@<account>.dfs.core.windows.net/feature_store/user_features/"

df = spark.read.format("delta").load(silver_path)
user_features = compute_user_features(df)
user_features.write.format("delta").mode("overwrite").save(feature_path)
