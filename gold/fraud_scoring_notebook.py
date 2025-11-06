# Databricks notebook for ML scoring
from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import RandomForestClassifier
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("GoldScoring").getOrCreate()
silver_path = "abfss://<container>@<account>.dfs.core.windows.net/silver/"
gold_path = "abfss://<container>@<account>.dfs.core.windows.net/gold/"

df = spark.read.format("delta").load(silver_path)

# Feature columns
feature_cols = ["amount"]  # extend with more features
assembler = VectorAssembler(inputCols=feature_cols, outputCol="features")
df = assembler.transform(df)

# Dummy ML model (replace with trained model)
rf = RandomForestClassifier(featuresCol="features", labelCol="risk_score")
model = rf.fit(df)  # in production, load pre-trained model

predictions = model.transform(df)
predictions.write.format("delta").mode("overwrite").save(gold_path)
