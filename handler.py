import json

def get(event, context):
    response = {
        "statusCode": 200,
        "body": json.dumps({"message": "Hello, This is a GET request, from Palak"}),
    }
    return response

def post(event, context):
    body = json.loads(event['body'])
    message = body.get('message', 'No message provided')
    response = {
        "statusCode": 200,
        "body": json.dumps({"message": f"Hello, This is a POST request with message: {message}"}),
    }
    return response
