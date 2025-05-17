from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr, lit
import random

spark = SparkSession.builder.remote("sc://sail-spark-server.sail.svc.cluster.local:50051").getOrCreate()


print("✅ Conectado a Spark:", spark.version)

df = spark.range(3)
df.show()
spark.stop()
