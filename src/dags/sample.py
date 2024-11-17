# ./src/dags/test_dag.py
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from datetime import datetime

with DAG(
    "sample_dag",
    default_args={"retries": 1},
    schedule_interval="@daily",
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:
    start = DummyOperator(task_id="start")
    end = DummyOperator(task_id="end")
    start >> end
