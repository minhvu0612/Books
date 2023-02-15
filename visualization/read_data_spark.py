from pyspark.sql import SparkSession

sparkSession = SparkSession.builder.appName("example-pyspark-read-and-write").getOrCreate()

df_load = sparkSession.read.csv('hdfs://localhost:9000/user/BTL/data/khoa_hoc_co_ban.csv', header = True)
df_load.select("Tác giả").show()


# Please change the path to the directory where the Hadoop is stored to your path