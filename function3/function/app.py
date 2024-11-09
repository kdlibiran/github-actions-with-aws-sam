import json

def lambda_handler(event, context):
    # Get the HTTP method from the event
    http_method = event.get('httpMethod')
    
    if http_method == 'GET':
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Hello from function3 - GET request"
            })
        }
    
    elif http_method == 'POST':
        # Get the request body
        try:
            body = json.loads(event.get('body', '{}'))
            return {
                "statusCode": 200,
                "body": json.dumps({
                    "message": "Hello from function3 - POST request",
                    "received_data": body
                })
            }
        except json.JSONDecodeError:
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "message": "Invalid JSON in request body"
                })
            }
    
    else:
        return {
            "statusCode": 405,
            "body": json.dumps({
                "message": "Method not allowed"
            })
        }
