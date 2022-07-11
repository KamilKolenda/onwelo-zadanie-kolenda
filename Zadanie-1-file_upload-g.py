import nasdaqdatalink
import boto3
import pandas as pd

access_key = 'acces key here'
secret_access_key = 'secret acces key here'
nasdaqdatalink.ApiConfig.api_key = 'api key here'

nasdaqdatalink.Database('ECONOMIST').bulk_download_to_file('C:/Users/stonk/Desktop/Python/')

s3_client = boto3.client('s3',
         aws_access_key_id=access_key,
         aws_secret_access_key= secret_access_key)
response = s3_client.upload_file('C:/Users/stonk/Desktop/Python/ECONOMIST.zip','onwelo-zadanie','ECONOMIST.zip')


