from pyspark.sql import SparkSession
from pyspark.sql.functions import col, date_format


def init_spark():
    sql = (
        SparkSession.builder.appName("tesing-app")
        .config("spark.jars", "/opt/spark-apps/postgresql-42.2.22.jar")
        .getOrCreate()
    )
    sc = sql.sparkContext
    return sql, sc


def main():
    url = "jdbc:postgresql://postgresdb:5432/product_wherehouse"
    properties = {
        "user": "postgres",
        "password": "admin",
        "driver": "org.postgresql.Driver",
    }
    file = "/opt/spark-data/retail_wherehouse.csv"
    sql, sc = init_spark()

    df = sql.read.load(file, format="csv", inferSchema="true", sep=",", header="true")
    df.show()

    # # Filter
    # df.filter(df.ITEM_TYPE == "WINE").write.jdbc(
    #     url=url, table="product_wherehouse", mode="append", properties=properties
    # ).save()


if __name__ == "__main__":
    main()
