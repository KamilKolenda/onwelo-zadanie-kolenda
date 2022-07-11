import json
import boto3


def lambda_handler(event, context):
    
    for i in event['Records']:
        action = i['eventName']
        bucket_name = i['s3']['bucket']['name']
        
    client = boto3.client('ses')
    
    subject = "Zadanie 2 - obiekt został dodany do S3 - Kamil Kolenda"
    body = '''
        <br>
        Nowy plik został dodany do S3. 
        '''.format(action)
    
    message = {'Subject': {'Data':subject}, 'Body': {'Html': {'Data':body}}}
    
    response = client.send_email(Source = 'kamil.contact@gmail.com', Destination = {'ToAddresses': ['monika.kulisz@onwelo.com']}, Message = message)
    
    
    
    
    
 
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
