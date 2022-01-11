import json

from models import User
from src.controller.cors import response
from pydantic_models import  UserModel


def create_user_main(event, context):
    response_body = {}
    try:
        data = json.loads(event["body"])
        UserModel(**data)
        user = User(**data).save()
        response_body["data"] = json.loads(user.to_json())
        response_body["status"] = True
        response_body["msg"] = "User created successfully"
        status_code = 200
    except Exception as e:
        response_body["msg"] = str(e)
        response_body["status"] = False
        status_code = 400
    return response(status_code, response_body)
