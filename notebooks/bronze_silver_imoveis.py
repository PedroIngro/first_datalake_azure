# Databricks notebook source
import pyspark.sql.functions as F
# import pyspark.sql.types as T

# COMMAND ----------

imoveis_raw_json = spark.read.json("dbfs:/mnt/dados/bronze/dados_brutos_imoveis.json")

# COMMAND ----------

imoveis_raw_json.printSchema()

# COMMAND ----------

imoveis_raw_json.limit(1).display()

# COMMAND ----------

imoveis_drop = imoveis_raw_json.drop('imagens', 'usuario')

# COMMAND ----------

imoveis_final = imoveis_drop.withColumn('id', F.col('anuncio.id'))

# COMMAND ----------

imoveis_final.limit(1).display()

# COMMAND ----------

print(imoveis_final.count())
imoveis_final.rdd.getNumPartitions()

# COMMAND ----------

sink = "dbfs:/mnt/dados/silver/dataset_imoveis"
imoveis_final.write.save(path = sink ,format='delta', mode = "overwrite")

# COMMAND ----------


