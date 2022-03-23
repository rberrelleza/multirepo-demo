import json

# reference, 
# https://travis.media/developing-aws-lambda-functions-locally-vscode/

def lambda_handler(event, context):
    first_name = event['first_name']
    last_name = event['last_name']
    greeting = event['greeting']

    message = f"{greeting} {first_name} {last_name}!"  

    return { 
        'message' : message
    }

    # sam build
    # sam local invoke HelloNameFunction -e events/events.json
    # sam deploy