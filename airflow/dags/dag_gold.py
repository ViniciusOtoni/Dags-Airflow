from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

def gold_processing():
    # Função para processamento de dados no estágio gold
    print("Processing Gold data...")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'gold_dag',
    default_args=default_args,
    description='DAG para processamento de dados em estágio gold',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(1),
    catchup=False,
) as dag:

    process_gold = PythonOperator(
        task_id='process_gold',
        python_callable=gold_processing,
    )
