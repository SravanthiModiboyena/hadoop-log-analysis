from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, round

# 1. Create Spark session
spark = SparkSession.builder \
    .appName("CSV to Parquet ETL") \
    .getOrCreate()

# 2. Extract - Read CSV
input_path = "data/input/sales.csv"
df = spark.read.option("header", "true").option("inferSchema", "true").csv(input_path)

print("Initial Data")
df.show()

# 3. Transform
# Remove rows with null amount
df_clean = df.filter(col("amount").isNotNull())

# Convert order_date to DateType
df_clean = df_clean.withColumn("order_date", to_date(col("order_date")))

# Add tax column (18%)
df_clean = df_clean.withColumn(
    "amount_with_tax",
    round(col("amount") * 1.18, 2)
)

# Aggregate total sales per customer
final_df = df_clean.groupBy("customer") \
    .sum("amount_with_tax") \
    .withColumnRenamed("sum(amount_with_tax)", "total_spent")

print("Transformed Data")
final_df.show()

# 4. Load - Write as Parquet
output_path = "output/customer_sales_parquet"

final_df.write.mode("overwrite").parquet(output_path)

print("ETL Pipeline Completed Successfully")

spark.stop()
