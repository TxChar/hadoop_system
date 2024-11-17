# Apache Hadoop, Spark, Airflow (Guideline)

## General
Container|Ports|URL
---|---|---
Hadoop|9870|http://localhost:9870/
Hadoop Cluster|8088|http://localhost:8088/
Spark-master|9090 7077|http://localhost:9090/
Spark-worker-1|9091|http://localhost:9091/
Spark-worker-2|9092|http://localhost:9092/
Airflow|8085|http://localhost:8085/
Postgresdb|5432|http://localhost:5432/
PgAdmin|5050|http://localhost:5050/

## Resource allowcate for SPARK
- CPU CORES each spark-worker is 1 core
- RAM for each spark-worker is 1024 MB
- RAM allocation for spark executors is 256mb
- RAM allocation for spark driver is 128mb

# COMMAND
## Build docker spark image
```sh
docker build -t cluster-apache-spark:3.0.2 .
```

## Build docker containers

```sh
docker-compose up -d --build --force-recreate
```


# Setup Hadoop HDFS and Spark
## HADOOP
```sh
docker exec -it namenode bash
#SETUP HDFS
export HADOOP_HOME=/opt/hadoop
export LD_LIBRARY_PATH=$HADOOP_HOME/lib/native:$LD_LIBRARY_PATH
hdfs dfs -mkdir /user
hdfs dfs -mkdir /user/root
hdfs dfs -chmod 777 /user/root
hdfs dfs -ls /
#TEST
echo "This is a test file for HDFS" > testfile.txt
hdfs dfs -put testfile.txt /user/root/
hdfs dfs -ls /user/root
```
## SPARK
```sh
docker exec -it spark-master bashhdfs dfs -mkdir /user
#SETUP ENV
export PATH=$PATH:/opt/spark/bin
export HADOOP_CONF_DIR=/opt/hadoop/etc/hadoop
export YARN_CONF_DIR=/opt/hadoop/etc/hadoop
```

## HDFS Files (Let's try to put your data to HDFS)
```sh
#On your PC
docker cp (local_file_for_tesing) namenode:/opt/hadoop/sample_data/(file_name_on_hadoop)
```
```sh
hadoop fs -mkdir /sample_data
wget https://raw.githubusercontent.com/metatron-app/metatron-doc-discovery/master/_static/data/sales-data-sample.csv
hadoop fs -put /opt/sample_data/sales-data-sample.csv /sample_data/
```
## Let's try Calculate!
### MapReduce (namenode)
```sh
yarn jar share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.6.jar pi 10 15
```

### SparkSubmit (spark-master) - [YarnMaster]
```sh
spark-submit   --master yarn   --deploy-mode cluster   --class org.apache.spark.examples.SparkPi   /opt/spark/examples/jars/spark-examples_2.12-3.0.2.jar
```

### SparkSubmit (spark-master) - [Master SingleNode]
```sh
spark-submit   --master spark://spark-master:7077   --deploy-mode client   --class org.apache.spark.examples.SparkPi   /opt/spark/examples/jars/spark-examples_2.12-3.0.2.jar
```

### SparkSubmit (spark-master) - [Master Cluster]
```sh
spark-submit --master spark://spark-master:7077 --deploy-mode cluster --jars /opt/spark-apps/postgresql-42.2.22.jar --driver-memory 1G --executor-memory 1G /opt/spark-apps/main.py
```

# REFERENCES
## Dataset
- https://www.kaggle.com/datasets/abdullah0a/retail-sales-data-with-seasonal-trends-and-marketing?resource=download
- https://www.kaggle.com/code/djonafegnem/chicago-crime-data-analysis/input

## HADOOP 
- https://medium.com/@bayuadiwibowo/deploying-a-big-data-ecosystem-dockerized-hadoop-spark-hive-and-zeppelin-654014069c82

## SPARK
- https://dev.to/mvillarrealb/creating-a-spark-standalone-cluster-with-docker-and-docker-compose-2021-update-6l4
- https://github.com/mvillarrealb/docker-spark-cluster