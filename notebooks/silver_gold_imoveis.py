# Databricks notebook source
import pyspark.sql.functions as F

# COMMAND ----------

imoveis_delta = spark.read.format('delta').load('dbfs:/mnt/dados/silver/dataset_imoveis')

# COMMAND ----------

imoveis_expanded = imoveis_delta.select(['anuncio.*', F.expr('id AS id_expr')])\
                             .drop('id')\
                             .withColumnRenamed('id_expr', 'id')
endereco_expanded = imoveis_expanded.select(['endereco.*', 'id'])

imoveis_final = imoveis_expanded.join(F.broadcast(endereco_expanded),
                                      ['id'],
                                      how = 'inner')\
                                 .drop('caracteristicas',)

# COMMAND ----------

path = 'dbfs:/mnt/dados/gold/dataset_imoveis'
imoveis_final.write.save(path = , format = 'delta', mode = 'overwrite')
