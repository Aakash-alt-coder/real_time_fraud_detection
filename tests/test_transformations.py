import unittest
from pyspark.sql import SparkSession
from silver.transformation_utils import deduplicate

class TestTransformations(unittest.TestCase):
    def setUp(self):
        self.spark = SparkSession.builder.appName("TestTransform").getOrCreate()
        data = [("1","txn1"),("1","txn1"),("2","txn2")]
        self.df = self.spark.createDataFrame(data, ["user_id","transaction_id"])

    def test_deduplicate(self):
        df_clean = deduplicate(self.df, ["transaction_id"])
        self.assertEqual(df_clean.count(), 2)

if __name__ == "__main__":
    unittest.main()
