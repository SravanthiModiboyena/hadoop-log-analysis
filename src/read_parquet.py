from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Read Parquet").getOrCreate()

df = spark.read.parquet("output/customer_sales_parquet")
df.show()

spark.stop()
