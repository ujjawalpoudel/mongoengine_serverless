import json

from models import User
from src.controller.cors import response


def read_users_main(event, context):
    response_body = {}
    try:
        parameters = event["queryStringParameters"]
        limit = int(parameters.pop("limit", 10))
        offset = int(parameters.pop("offset", 0))
        # * limit means items per page
        # * offset means skip that many rows before beginning to return rows
        users = User.objects.skip(offset).limit(limit)
        response_body["data"] = json.loads(users.to_json())
        response_body["msg"] = "User query successfully"
        response_body["status"] = True
        status_code = 200
    except Exception as e:
        response_body["msg"] = str(e)
        response_body["status"] = False
        status_code = 400
    return response(status_code, response_body)
