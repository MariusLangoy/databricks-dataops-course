# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC # Deploy tasks
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Study: deployment.yml
# MAGIC
# MAGIC Look at `orgs/acme/domains/transport/projects/taxinyc/flows/prep/revenue/deployment.yml`.
# MAGIC It defines the job which will run the pipeline.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Task: Run dev deploy
# MAGIC
# MAGIC 1. Go to the notebook orgs/acme/domains/transport/projects/taxinyc/flows/prep/revenue/deploy
# MAGIC 2. Connect to serverless compute.
# MAGIC 3. Run the cells up to and including deploying and running the dev job.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Task: Look for the job under Job Runs
# MAGIC
# MAGIC Job Runs are on the side menu

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Task: Run the job by pressing the run button in the UI

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Task: What is the difference between a job and a job run?

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC A job is a scheduled task or a set of tasks, while a job run is an instance of the execution of that job.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Task: How was the job name composed?
# MAGIC
# MAGIC The job name is composed of a prefix, a unique identifier, and a suffix.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Answer here...
