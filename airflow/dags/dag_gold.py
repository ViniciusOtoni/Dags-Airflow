from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import timedelta
import sys

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

sys.path.append('/opt/airflow/ETL/gold')
from main import GoldETL

def gold_processing():
    try:
        path_df = '/opt/airflow/data/d03_silver/movies_complete_silver.csv'
        output_dir = '/opt/airflow/data/d04_gold/'
        file_name = 'movies_best_worst_gold.csv'
        etl = GoldETL(path_df, output_dir, file_name, len_df=20, orderby="Movie_Popularity", ascending=False, min_bud=200, min_votes=200)
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
    'gold_dag',
    default_args=default_args,
    description='DAG para processamento de dados em estágio gold',
    schedule_interval="@daily",
    start_date=days_ago(1),
    catchup=False,
) as dag:

    process_gold = PythonOperator(
        task_id='process_gold',
        python_callable=gold_processing,
        provide_context=True
    )
