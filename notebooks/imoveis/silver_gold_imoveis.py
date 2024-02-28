# Databricks notebook source
# MAGIC %md
# MAGIC ### Projeto Imóveis Alura
# MAGIC ** Isso faz parte do projeto datalake do curso de Data Factory da Alura **
# MAGIC
# MAGIC ** É um notebook simples explicando o básico de integração entre o databricks e o datafactory **
# MAGIC
# MAGIC ** Gravação da camada Silver para a camada Gold **

# COMMAND ----------

# Importando biblioteca Functions
import pyspark.sql.functions as F

# COMMAND ----------

# Leitura dos dados na camada silver
imoveis_delta = spark.read.format('delta').load('dbfs:/mnt/dados/silver/dataset_imoveis')

# COMMAND ----------

# Realizando a expansão das colunas assim criando uma em cada objeto do JSON
# Realizando join entre o dataset expandido e o dataset possuindo a expansão do endereço
imoveis_expanded = imoveis_delta.select(['anuncio.*', F.expr('id AS id_expr')])\
                             .drop('id')\
                             .withColumnRenamed('id_expr', 'id')
endereco_expanded = imoveis_expanded.select(['endereco.*', 'id'])

imoveis_final = imoveis_expanded.join(F.broadcast(endereco_expanded),
                                      ['id'],
                                      how = 'inner')\
                                 .drop('caracteristicas',)

# COMMAND ----------

# Gravação no Path abaixo na camada Gold
path = 'dbfs:/mnt/dados/gold/dataset_imoveis'
imoveis_final.write.save(path = path , format = 'delta', mode = 'overwrite')
