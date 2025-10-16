import boto3
import os

s3 = boto3.client('s3')

def lambda_handler(event, context):
    
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    
    key = event['Records'][0]['s3']['object']['key']
    
    
    destination_bucket = os.environ['DEST_BUCKET']
    
    
    response = s3.get_object(Bucket=source_bucket, Key=key)
    content = response['Body'].read().decode('utf-8')
    
    
    transformed = content.upper()
    
    
    new_key = f"processed/{key}"
    
    
    s3.put_object(Bucket=destination_bucket, Key=new_key, Body=transformed.encode('utf-8'))
    
    return {
        'statusCode': 200,
        'body': f'Arquivo {key} processado e salvo como {new_key} no bucket {destination_bucket}'
    }
