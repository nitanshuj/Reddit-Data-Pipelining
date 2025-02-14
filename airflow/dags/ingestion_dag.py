# airflow/dags/ingestion_dag.py
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import os

default_args = {
    'owner': 'admin',
    'retries': 3,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    'reddit_data_ingestion',
    default_args=default_args,
    description='Daily Reddit data collection',
    schedule_interval='@daily',
    start_date=datetime(2025, 2, 12)
) as dag:
    
    run_producer = PythonOperator(
        task_id='run_reddit_producer',
        python_callable=lambda: os.system('python src/producers/reddit_producer.py')
    )
    
    setup_s3 = PythonOperator(
        task_id='setup_s3_infrastructure',
        python_callable=lambda: os.system('python scripts/s3_setup.py')
    )

    setup_s3 >> run_producer
