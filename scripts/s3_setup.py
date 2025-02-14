# scripts/s3_setup.py

import boto3
import os

from botocore.exceptions import ClientError


s3 = boto3.client('s3',
                  aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
                  aws_secret_access_key=os.getenv('AWS_SECRET_KEY'))

def create_bucket_with_lifecycle():
    bucket_name = os.getenv('S3_BUCKET_NAME')
    try:
        s3.create_bucket(Bucket=bucket_name)
        s3.put_bucket_lifecycle_configuration(
            Bucket=bucket_name,
            LifecycleConfiguration={
                'Rules': [{
                    'ID': '7-day-expiration',
                    'Status': 'Enabled',
                    'Prefix': '',
                    'Expiration': {'Days': 7},
                    'Transitions': []
                }]
            }
        )
        print(f"Bucket {bucket_name} created with lifecycle rules")
    except ClientError as e:
        print(f"Error creating bucket: {e}")
