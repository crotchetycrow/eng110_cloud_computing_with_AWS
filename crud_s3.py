import boto3
import botocore
import logging
from botocore.exceptions import ClientError
import os


def create_bucket(bucket_name, region=None):
    if region is None:
        s3_client = boto3.client('s3')
        s3_client.create_bucket(Bucket=bucket_name)
    else:
        s3_client = boto3.client('s3', region_name=region)
        location = {'LocationConstraint': region}
        s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)


def read_file(bucket, file_name):
    s3 = boto3.resource('s3')
    s3_obj = s3.Bucket(bucket).Object(file_name).get()
    text = s3_obj['Body'].read().decode('utf-8')
    return text


def retrieve_file(bucket, object_name, file_name):
    s3 = boto3.client('s3')
    s3.download_file(bucket, object_name, file_name)


def upload_file(file_name, bucket, object_name=None):
    if object_name is None:
        object_name = os.path.basename(file_name)
    s3_client = boto3.client('s3')
    s3_client.upload_file(file_name, bucket, object_name)


def delete_file(bucket, file_name):
    s3 = boto3.client('s3')
    resp = s3.delete_object(Bucket=bucket, Key=file_name)
    return resp


def delete_bucket(bucket):
    s3 = boto3.client('s3')
    resp = s3.delete_bucket(Bucket=bucket)

# create_bucket('eng110-jack-test', 'eu-west-1')
# read_file('eng110-jack-test', 'test.txt')
# retrieve_file('eng110-jack-test', 'test.txt', 'test.txt')
# upload_file('test.txt', 'eng110-jack-test', 'test.txt')
# delete_file('eng110-jack-test', 'test.txt')
# delete_bucket('eng110-jack-test')
