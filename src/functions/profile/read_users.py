import json

from models import User
from src.controller.cors import response


def read_users_main(event, context):
    response_body = {}
    try:
        response_body["data"] = json.loads(User.objects().to_json())
        response_body["msg"] = "User query successfully"
        response_body["status"] = True
        status_code = 200
    except Exception as e:
        response_body["msg"] = str(e)
        response_body["status"] = False
        status_code = 400
    return response(status_code, response_body)
