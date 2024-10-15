import json
import boto3
import os

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    bucket_name = os.environ['toru010-tf']
    # List objects in the specified bucket
    try:
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        objects = response.get('Contents', [])
        object_list = [obj['Key'] for obj in objects]  # List the object keys (names)
        return {
            'statusCode': 200,
            'body': json.dumps({
                'bucket': bucket_name,
                'objects': object_list
            })
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e)
            })
        }
