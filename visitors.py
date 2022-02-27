import boto3
import json

def lambda_handler(event, context):
    def getCounter(event, context):
        updateCounter()
        # Get the service resource.
        dynamodb = boto3.resource('dynamodb')

        table = dynamodb.Table('visitors')
        response = table.get_item(
            Key={
                'id'
            }
        )


def updateCounter():
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('visitors')
    response = table.update_item(
        Key={
            'id'
        },
        AttributeUpdates={
            'counter': {
                'Value': 1,
                'Action': 'ADD'
            }
        }
    )
    response = {
        'statusCode': 200,
        'body': json.dumps(data),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },

    }
    return json.dumps(response)
