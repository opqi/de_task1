import os
import boto3
from botocore.exceptions import NoCredentialsError
from dotenv import load_dotenv


dotenv_path = '.env_s3'
load_dotenv(dotenv_path)

s3_server_host = 'localhost'
s3_server_port = 9000
s3_access_key = os.getenv('MINIO_ROOT_USER')
s3_secret_key = os.getenv('MINIO_ROOT_PASSWORD')

s3_bucket_name = 'loadcsvbucket'
s3_object_key = 'load_data.csv'
local_file_path = './data/load_data.csv'

def create_s3_bucket():
    s3_client = boto3.client(
        "s3",
        endpoint_url=f"http://{s3_server_host}:{s3_server_port}",
        aws_access_key_id=s3_access_key,
        aws_secret_access_key=s3_secret_key,
    )

    try:
        s3_client.create_bucket(Bucket=s3_bucket_name)
        print(f"S3 bucket '{s3_bucket_name}' created successfully.")
    except NoCredentialsError as e:
        print(f"Failed to create S3 bucket. No valid credentials. Error: {e}")
    except Exception as e:
        print(f"Failed to create S3 bucket. Error: {e}")

def upload_file_to_s3(local_file_path, s3_bucket_name, s3_object_key):
    s3_client = boto3.client(
        "s3",
        endpoint_url=f"http://{s3_server_host}:{s3_server_port}",
        aws_access_key_id=s3_access_key,
        aws_secret_access_key=s3_secret_key,
    )

    try:
        s3_client.upload_file(local_file_path, s3_bucket_name, s3_object_key)
        print(f"File '{local_file_path}' uploaded to S3 bucket '{s3_bucket_name}' with key '{s3_object_key}'.")
    except NoCredentialsError as e:
        print(f"Failed to upload file. No valid credentials. Error: {e}")
    except Exception as e:
        print(f"Failed to upload file. Error: {e}")

def list_objects_in_s3_bucket():
    s3_client = boto3.client(
        "s3",
        endpoint_url=f"http://{s3_server_host}:{s3_server_port}",
        aws_access_key_id=s3_access_key,
        aws_secret_access_key=s3_secret_key,
    )

    try:
        response = s3_client.list_objects(Bucket=s3_bucket_name)
        objects = response.get("Contents", [])

        if objects:
            print(f"Objects in S3 bucket '{s3_bucket_name}':")
            for obj in objects:
                print(obj["Key"])
        else:
            print(f"S3 bucket '{s3_bucket_name}' is empty.")
    except NoCredentialsError as e:
        print(f"Failed to list objects. No valid credentials. Error: {e}")
    except Exception as e:
        print(f"Failed to list objects. Error: {e}")


def delete_file_from_s3(s3_bucket_name, s3_object_key):
    s3_client = boto3.client(
        "s3",
        endpoint_url=f"http://{s3_server_host}:{s3_server_port}",
        aws_access_key_id=s3_access_key,
        aws_secret_access_key=s3_secret_key,
    )

    try:
        s3_client.delete_object(Bucket=s3_bucket_name, Key=s3_object_key)
        print(f"File '{s3_object_key}' deleted from S3 bucket '{s3_bucket_name}'.")
    except NoCredentialsError as e:
        print(f"Failed to delete file. No valid credentials. Error: {e}")
    except Exception as e:
        print(f"Failed to delete file. Error: {e}")


if __name__ == '__main__':
    create_s3_bucket()
    upload_file_to_s3(local_file_path, s3_bucket_name, s3_object_key)
    list_objects_in_s3_bucket()
