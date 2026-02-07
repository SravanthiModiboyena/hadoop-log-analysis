<<<<<<< HEAD
# Hadoop Log File Analysis (Python)

## Description
This project analyzes server log files using Hadoop Streaming with Python.
It counts HTTP 4xx and 5xx error responses from log data stored in HDFS.

## Technologies Used
- Hadoop (HDFS, MapReduce, YARN)
- Hadoop Streaming
- Python 3

## Use Case
Log analytics for identifying client and server errors in distributed systems.

## How to Run
1. Upload logs to HDFS
2. Run Hadoop Streaming job with mapper and reducer scripts
3. View output from HDFS
=======
# Spark ETL Pipeline (CSV to Parquet)

## Description
This project demonstrates a Spark ETL pipeline using PySpark.

## Steps
- Extract data from CSV
- Clean null values
- Apply transformations
- Aggregate customer sales
- Store output in Parquet format

## Technologies
- Apache Spark
- PySpark
- Parquet

## How to Run
```bash
spark-submit src/etl_csv_to_parquet.py
>>>>>>> 8b5d531 (Add Spark ETL pipeline: CSV to Parquet)

