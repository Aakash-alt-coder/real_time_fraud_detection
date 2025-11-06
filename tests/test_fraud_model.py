import unittest
from pyspark.sql import SparkSession

class TestFraudModel(unittest.TestCase):
    def setUp(self):
        self.spark = SparkSession.builder.appName("TestFraudModel").getOrCreate()

    def test_dummy_model(self):
        data = [(100.0,)]
        df = self.spark.createDataFrame(data, ["amount"])
        self.assertEqual(df.count(), 1)

if __name__ == "__main__":
    unittest.main()
