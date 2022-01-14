import json
import math

from models import User
from pydantic_models import PaginationModel
from src.controller.cors import response
from src.controller.helpers import skiplimit


def read_users_main(event, context):
    response_body = {}
    try:
        parameters = event["queryStringParameters"]
        if(parameters is not None):
            PaginationModel(**parameters)
            page_size = int(parameters.pop("page_size", 10))
            page_num = int(parameters.pop("page_num", 1))
        else:
            page_size = 10
            page_num = 1

        offset, limit = skiplimit(page_size, page_num)

        users = User.objects.skip(offset).limit(limit)
        user_count = users.count()

        response_body["data"] = json.loads(users.to_json())
        response_body["total_page_num"] = math.ceil(user_count / page_size)
        response_body["total_documents"] = user_count
        response_body["msg"] = "User query successfully"
        response_body["status"] = True
        status_code = 200
    except Exception as e:
        response_body["msg"] = str(e)
        response_body["status"] = False
        status_code = 400
    return response(status_code, response_body)
