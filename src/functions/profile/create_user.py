import json

from models import User
from src.controller.cors import response


def create_user_main(event, context):
    body = {}
    try:
        data = json.loads(event['body'])
        print(data)
        user = User(**data).save()
        body["data"] = json.loads(user.to_json())
        body["status"] = True
        body["msg"] = "User created successfully"
        status_code = 200
    except Exception as e:
        body["msg"] = str(e)
        body["status"] = False
        status_code = 400
    return response(status_code, body)

