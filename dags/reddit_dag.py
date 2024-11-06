from datetime import datetime
import os, sys
from airflow import DAG
from airflow.operators.python import PythonOperator


sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# User Defined
from pipelines.reddit_pipeline import reddit_pipeline



default_args = {
    'owner': 'Nitanshu Joshi',
    'start_date': datetime(2024, 9, 22)  # Year, Month, Day
    }

file_postfix = datetime.now().strftime("%Y%m%d")


dag = DAG(
    dag_id = 'etl_reddit_pipeline',
    default_args = default_args,
    schedule_interval = '@daily', 
    catchup=False,
    tags = ['reddit', 'etl', 'pipeline', 'reddit-etl-pipeline']
)

# Extraction from Reddit
extract = PythonOperator(
    task_id='reddit_extraction',
    python_callable=reddit_pipeline,
    op_kwargs={
        'file_name': f'reddit_{file_postfix}',
        'subreddit': 'dataengineering',
        'time_filter': 'day',
        'limit': 100        # 100 posts in the sub-reddit
    },
    dag = dag
    
)