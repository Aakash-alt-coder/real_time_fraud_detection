import unittest
from pyspark.sql import SparkSession

class TestIngestion(unittest.TestCase):
    def setUp(self):
        self.spark = SparkSession.builder.appName("TestIngestion").getOrCreate()

    def test_read_bronze(self):
        df = self.spark.read.format("delta").load("sample_data/transactions_sample.csv")
        self.assertGreater(df.count(), 0)

if __name__ == "__main__":
    unittest.main()
