# Databricks notebook source
dbutils.fs.mkdirs("/mnt/dados")

# COMMAND ----------

dbutils.fs.ls("/mnt")

# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth",
          "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
          "fs.azure.account.oauth2.client.id": "4ff6e290-442b-4ce8-95aa-6863422ded50",
          "fs.azure.account.oauth2.client.secret": "6D_8Q~R3axnBWhjcpsKIOGXpjY5BV9AOkbzVqb~V",
          "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/dfb66dc4-3f3c-492c-991d-727dbd1c89d4/oauth2/token"}

# Optionally, you can add <directory-name> to the source URI of your mount point.
dbutils.fs.mount(
  source = "abfss://imoveis@firstdatalakealura.dfs.core.windows.net/",
  mount_point = "/mnt/dados",
  extra_configs = configs)

# COMMAND ----------

dbutils.fs.ls("/mnt/dados")

# COMMAND ----------


