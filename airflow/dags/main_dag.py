from airflow import DAG
from airflow.operators.dagrun_operator import TriggerDagRunOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'main_dag',
    default_args=default_args,
    description='DAG principal para orquestrar a execução das DAGs bronze, silver e gold',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(1),
    catchup=False,
) as dag:

    trigger_bronze = TriggerDagRunOperator(
        task_id='trigger_bronze',
        trigger_dag_id='bronze_dag',
    )

    # trigger_silver = TriggerDagRunOperator(
    #     task_id='trigger_silver',
    #     trigger_dag_id='silver_dag',
    # )

    # trigger_gold = TriggerDagRunOperator(
    #     task_id='trigger_gold',
    #     trigger_dag_id='gold_dag',
    # )

    # Define as dependências
    trigger_bronze 
    #>> trigger_silver >> trigger_gold
