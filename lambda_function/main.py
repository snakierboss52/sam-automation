import json

def app(event, context):
    return {
        'statusCode': 200,
        'body': 'This is my version number 2'
    }