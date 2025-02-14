#!/bin/bash

# Create directories
mkdir -p docker/kafka
mkdir -p src/producers src/consumers src/spark
mkdir -p airflow/dags
mkdir -p research_notebooks
mkdir -p dashboard
mkdir -p monitoring/grafana_dashboards
mkdir -p .github/workflows

# Create files
touch docker/docker-compose.yml
touch src/producers/reddit_producer.py
touch src/consumers/spark_consumer.py
touch src/spark/sentiment_analysis.py
touch src/spark/topic_modeling.py
touch airflow/dags/ingestion_dag.py
touch airflow/dags/processing_dag.py
touch research_notebooks/analysis.ipynb
touch dashboard/reddit_analysis.pbix
touch monitoring/grafana_dashboards/pipeline_metrics.json
touch .github/workflows/ci_cd.yml

echo "Folder structure and files created successfully"
