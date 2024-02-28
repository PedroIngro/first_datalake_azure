# Databricks notebook source
# MAGIC %md
# MAGIC ### Notebook criado para testes de Data Factory

# COMMAND ----------

import pyspark.sql.functions as F
import pyspark.sql.types as T

# COMMAND ----------

kc_house_data = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv("dbfs:/mnt/dados/bronze/kc_house_data.csv")

# COMMAND ----------

kc_house_data_partition = kc_house_data.withColumn('year', F.substring(F.col('date'), 0, 4))
kc_house_data_partition = kc_house_data_partition.withColumn('year', F.col('year').cast(T.IntegerType()))\
                                                 .filter(F.col('year') == 2014)

# COMMAND ----------

sink = "dbfs:/mnt/dados/silver/test_storage_trigger"
kc_house_data_partition.coalesce(1).write.partitionBy('year').save(path=sink, format="parquet", mode="overwrite")

