# HADOOP AND SPARK (NameNode)

## URL PATHS
- http://localhost:9870/
- http://localhost:8088/

## COMMAND
- docker-compose up -d
- docker-compose up -d --build --force-recreate
- docker cp spark-3.5.0.bin-hadoop3.tgz hadoop_namenode_1:/opt/spark/spark-3.5.0.bin-hadoop3.tgz
- tar -zxvf spark-3.5.0.bin-hadoop3.tgz


# HADOOP HDFS AND MAPREDUCE
- HDFS Files
hadoop fs -mkdir /sample_data
wget https://raw.githubusercontent.com/metatron-app/metatron-doc-discovery/master/_static/data/sales-data-sample.csv
hadoop fs -put /opt/sample_data/sales-data-sample.csv /sample_data/

- MapReduce
namenode $yarn jar share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.6.jar pi 10 15

# SPARK
- Spark Submit
/opt/spark/spark-3.5.0-bin-hadoop3/bin/spark-submit --master local --class org.apache.spark.examples.SparkPi /opt/spark/spark-3.5.0-bin-hadoop3/examples/jars/spark-examples_2.12-3.5.0.jar
