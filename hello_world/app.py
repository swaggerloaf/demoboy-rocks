import json

# import requests


def lambda_handler(event, context):

    if True:
        raise Exception("This will cause a deployment rollback")
    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "This is carnary deployment",
            }
        ),
    }
