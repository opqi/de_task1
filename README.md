# de_task1

## Create folders
mkdir data data_minio

## Run services
docker-compose up -d

## Install requirements
pip install -r requirements

## Import template to nifi
Upload template etl.xml to nifi

Crete template etl and enable CSVReader and DBCPConnectionPool (set Password from .env_postgres)

Set Access Key ID and Secret Access Key in ListS3 and FetchS3Object form .env_s3

## Generate data:
python ./scripts/gen_data.py

## Init bucket and insert data to the bucket:
python ./scripts/load_file_to_s3.py
