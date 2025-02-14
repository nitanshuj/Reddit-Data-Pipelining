# src/producers/reddit_producer.py
import praw
from kafka import KafkaProducer
import json
import os
from datetime import datetime

reddit = praw.Reddit(
    client_id=os.getenv('REDDIT_CLIENT_ID'),
    client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
    user_agent=os.getenv('REDDIT_USER_AGENT')
)

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def collect_reddit_data(subreddits):
    for subreddit_name in subreddits:
        subreddit = reddit.subreddit(subreddit_name)
        
        # Collect posts
        for post in subreddit.new(limit=50):
            producer.send('posts', {
                'id': post.id,
                'title': post.title,
                'score': post.score,
                'url': post.url,
                'num_comments': post.num_comments,
                'created_utc': post.created_utc,
                'subreddit': subreddit_name,
                'collected_at': datetime.utcnow().isoformat()
            })
        
        # Collect comments
        for comment in subreddit.comments(limit=20):
            producer.send('comments', {
                'id': comment.id,
                'body': comment.body,
                'score': comment.score,
                'post_id': comment.submission.id,
                'subreddit': subreddit_name,
                'collected_at': datetime.utcnow().isoformat()
            })

if __name__ == "__main__":
    collect_reddit_data(['datascience', 'machinelearning', 'artificial'])
