from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

def silver_processing():
    # Função para processamento de dados no estágio silver
    print("Processing Silver data...")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'silver_dag',
    default_args=default_args,
    description='DAG para processamento de dados em estágio silver',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(1),
    catchup=False,
) as dag:

    process_silver = PythonOperator(
        task_id='process_silver',
        python_callable=silver_processing,
    )
