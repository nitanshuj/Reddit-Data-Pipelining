
# Export from User Defined Functions
from utils.constants import CLIENT_ID, SECRET

from etls.reddit_etl import connect_reddit
from etls.reddit_etl import extract_posts



def reddit_pipeline(filename: str, subreddit: str, time_filter = 'day', limit=None):

    # Connecting to reddit instance
    instance = connect_reddit(CLIENT_ID, SECRET, 'Cloudys Agent')

    # Extraction
    posts = extract_posts(reddit_instance=instance, subreddit=subreddit, time_filter='day', limit=None)

    # Transformation


    # Loading to csv

    
    # return file_path
    pass