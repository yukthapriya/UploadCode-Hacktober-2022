from pyspark.sql import SparkSession
spark = (SparkSession
.builder
.appName("<app_name>")
.getOrCreate())
#sparksession
