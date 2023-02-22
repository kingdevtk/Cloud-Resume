import json
import boto3

client = boto3.client('dynamodb')

def lambda_handler(event, context):
  data = client.scan(
    TableName='VisitorCount'
  )

  response = {
      'statusCode': 200
      }


  return response
