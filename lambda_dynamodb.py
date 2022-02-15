import boto3
import json

client = boto3.client('dynamodb')

def lambda_handler(event, context):
  data = client.scan(
    TableName='VisitorCount'
    )
