# Databricks notebook source
import pyspark.sql.functions as F
import pyspark.sql.types as T

# COMMAND ----------

kc_house_data = spark.read.parquet("dbfs:/mnt/dados/silver/test_storage_trigger")

# COMMAND ----------

sink = "dbfs:/mnt/dados/gold/test_storage_trigger"
kc_house_data.coalesce(1).write.partitionBy('year').save(path=sink, format="parquet", mode="overwrite")

