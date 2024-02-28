# Databricks notebook source
# MAGIC %md
# MAGIC ### Projeto Imóveis Alura
# MAGIC ** Isso faz parte do projeto datalake do curso de Data Factory da Alura **
# MAGIC
# MAGIC ** É um notebook simples explicando o básico de integração entre o databricks e o datafactory **
# MAGIC
# MAGIC ** Gravação da camada Bronze para a camada Silver **

# COMMAND ----------

# Importando biblioteca Functions
import pyspark.sql.functions as F

# COMMAND ----------

# Leitura do Json presente na camada bronze
imoveis_raw_json = spark.read.json("dbfs:/mnt/dados/bronze/dados_brutos_imoveis.json")

# COMMAND ----------

# Printar o Schema da tabela
imoveis_raw_json.printSchema()

# COMMAND ----------

# Visualização de como a tabela se formou
imoveis_raw_json.limit(1).display()

# COMMAND ----------

# Realizando a retirada das colunas dentro do comando drop
imoveis_drop = imoveis_raw_json.drop('imagens', 'usuario')

# COMMAND ----------

# Criação de uma coluna possuindo o ID do Anúncio
imoveis_final = imoveis_drop.withColumn('id', F.col('anuncio.id'))

# COMMAND ----------

# Visualizando forma final da tabela a ser gravada
imoveis_final.limit(1).display()

# COMMAND ----------

# Realizando a contagem de dados e checando quantas partições serão gravadas
print(imoveis_final.count())
print(imoveis_final.rdd.getNumPartitions())

# COMMAND ----------

# Caminho para gravação no formato delta
sink = "dbfs:/mnt/dados/silver/dataset_imoveis"
imoveis_final.write.save(path = sink ,format='delta', mode = "overwrite")
