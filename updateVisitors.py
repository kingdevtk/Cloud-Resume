# grabs the record with key ‘visitor_id’ and then adds 1 to the ‘visitor_count’ value of the record, sending the updated ‘visitor_count’ as a response
import json
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Visitors')
def lambda_handler(event, context):
    response = table.get_item(Key={
            'visitor_id':'0'
    })
    record_count = response['Item']['visitor_count']
    record_count = record_count + 1
    print(record_count)
    response = table.put_item(Item={
            'visitor_id':'0',
            'visitor_count': record_count
    })
    
    return "Records added successfully!"
