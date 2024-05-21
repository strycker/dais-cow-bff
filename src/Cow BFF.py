# Databricks notebook source
# MAGIC %md
# MAGIC ## First we install Python packages and initialize our globals

# COMMAND ----------

# MAGIC %pip install -r ../requirements.txt
# MAGIC %load_ext autoreload
# MAGIC %autoreload 2

# COMMAND ----------

# load table into spark dataframe
cows_bff = spark.read.table("db.cows_bff")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Lets compute meal overlap

# COMMAND ----------

from cow_bff.heatmap import compute_heatmap

df = compute_heatmap(cows_bff)
display(df.limit(10))

# COMMAND ----------

# MAGIC %md
# MAGIC # Display Heatmap

# COMMAND ----------

# DBTITLE 1,Verify with notebook viz
display(df)

# COMMAND ----------

