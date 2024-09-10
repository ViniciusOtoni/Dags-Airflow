from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import timedelta




def bronze_processing():
    path_df = '/opt/airflow/data/d01_raw/movies_complete.csv'
    output_dir = '/opt/airflow/data/d02_bronze/'
    file_name = 'movies_complete_bronze.csv'

    etl = BronzeETL(path_df, output_dir, file_name)

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

with DAG(
    'bronze_dag',
    default_args=default_args,
    description='DAG para processamento de dados em estágio bronze',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(1),
    catchup=False,
) as dag:

    process_bronze = PythonOperator(
        task_id='process_bronze',
        python_callable=bronze_processing,
    )
