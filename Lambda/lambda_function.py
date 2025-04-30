import json
import boto3

def lambda_handler(event, context):
    s3_bucket = event['bucket']
    s3_key = event['key']
    
    client = boto3.client('rekognition')
    response = client.detect_labels(
        Image={'S3Object': {'Bucket': s3_bucket, 'Name': s3_key}},
        MaxLabels=10,
        MinConfidence=70
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps(response['Labels'], indent=2)
    }
