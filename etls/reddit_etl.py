import sys
import numpy as np, pandas as pd

import praw
from praw import Reddit

def connect_reddit(client_id, client_secret, user_agent) -> Reddit:

    try:
        reddit = praw.Reddit(client_id=client_id,
                        client_secret=client_secret,
                        user_agent=user_agent)
        print("Connected to reddit!")
        return reddit
    except Exception as e:
        print("Failed to connect to reddi : ", e)
        sys.exit(1)



def extract_posts(reddit_instance: Reddit, subreddit: str, time_filter: str, limit=None):
    subreddit = reddit_instance.subreddit(subreddit)
    posts = subreddit.top(time_filter=limit)
    print(posts) # only for checking the process
    post_list = []

    # for post in posts: 
    #     post_list.append({
    #         'title': post.title,
    #         'author': post.author.name,
    #         'comments_count': post.num_comments,
    #         'score': post.score,
    #         'url': post.url
    #     })
    pass