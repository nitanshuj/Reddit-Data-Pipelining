# reddit-sentiment-analysis-and-topic-modelling
Reddit Sentiment Analysis and Topic Modelling

## Project Overview

This project aims to create a comprehensive data engineering pipeline that streams, analyzes, and visualizes real-time data from Reddit. By leveraging the PRAW API, the pipeline captures the top 50 latest posts and the 20 most upvoted comments from a selection of 5-10 subreddits. 

## Technology Stack

- **Data Streaming**: Apache Kafka
- **Orchestration**: Apache Airflow
- **Data Processing**: Apache Spark
- **Storage**: AWS S3
- **Data Visualization**: Tableau or PowerBI for dashboards; Grafana for monitoring

## Analysis Objectives

The pipeline will perform several key analyses:

- **Sentiment Analysis**: Classifying comments and posts into Positive, Negative, or Neutral sentiments to gauge community reactions.
  
- **Topic Modeling**: Identifying the most frequently used words and topics within the selected subreddits, providing insights into trending discussions.

## Dashboard Features

A dynamic dashboard will be built to visualize the analysis results, featuring:

- **Top Topics Discussed**: Highlighting the most prevalent themes within the selected subreddits.
  
- **Sentiment Distribution**: Displaying how sentiments are scattered across different posts and comments, allowing for quick insights into community mood.
