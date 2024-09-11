from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import timedelta
import logging
import sys

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

sys.path.append('/opt/airflow/ETL/silver')

from main import SilverETL

def silver_processing():
    try:
        path_df = '/opt/airflow/data/d02_bronze/movies_complete_bronze.csv'
        output_dir = '/opt/airflow/data/d03_silver/'
        file_name = 'movies_complete_silver.csv'
        etl = SilverETL(path_df, output_dir, file_name)
        logger.info("Processo ETL completo")
    except Exception as e:
        logger.error(f"Erro no ETL: {e}")
        raise

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'silver_dag',
    default_args=default_args,
    description='DAG para processamento de dados em estágio silver',
    schedule_interval="@daily",
    start_date=days_ago(1),
    catchup=False,
) as dag:
    
  

    process_silver = PythonOperator(
        task_id='process_silver',
        python_callable=silver_processing,
        provide_context=True, 
    )


