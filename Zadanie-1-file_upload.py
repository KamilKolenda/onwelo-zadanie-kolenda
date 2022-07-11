import nasdaqdatalink
import boto3
import pandas as pd
import os

access_key = 'AKIA4UEYLQ2RSJBWW7NK'
secret_access_key = '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'
nasdaqdatalink.ApiConfig.api_key = 'gsxvQ9bJTagPNfsNWu_x'
directory = os.getcwd()

nasdaqdatalink.Database('ECONOMIST').bulk_download_to_file('C:/Users/stonk/Desktop/Python/')

s3_client = boto3.client('s3')
response = s3_client.upload_file('C:/Users/stonk/Desktop/Python/ECONOMIST.zip','kolenda-zadanie','ECONOMIST.zip')
