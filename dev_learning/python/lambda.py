import http
import json
from webbrowser import get
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Visitors")

def handler(event, context):
    http_method = event.get("http_method")
    
    if http_method == "GET":
        return get_visitors()
    
    if http_method == "POST":
        update_vistors()
        return get_visitors()

def get_visitors() -> int:
    response = table.get_item(Key={
       "visitor_id":"0"
    })
    return response["Item"]["visitor_count"]

def update_vistors():
    record_count = get_visitors()
    record_count = record_count + 1
    
    print(record_count)
    
    table.put_item(Item={
        "visitor_id":"0",
        "visitor_count": record_count