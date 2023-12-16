# de_task1

## Run services
docker-compose up -d

## Install requirements
pip install -r requirements

## Import template to nifi
Upload template etl.xml to nifi
Crete template etl and enable CSVReader and DBCPConnectionPool

## Generate data:
python ./scripts/gen_data.py

## Init bucket and insert data to the bucket:
python ./scripts/load_file_to_s3.py
