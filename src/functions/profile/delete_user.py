import json

from models import User
from src.controller.cors import response
from src.validators import DeleteUserModel


def delete_user_main(event, context):
    response_body = {}
    try:
        data = json.loads(event["body"])
        # DeleteUserModel(**data)
        user_id = data.pop("id", None)
        if user_id is not None:
            User.objects.get(id=user_id).delete()
            response_body["msg"] = "User deleted successfully"
            response_body["status"] = True
        else:
            response_body["msg"] = "User Id should pass for deletion operation"
            response_body["status"] = False
        status_code = 200
    except Exception as e:
        response_body["msg"] = str(e)
        response_body["status"] = False
        status_code = 400
    return response(status_code, response_body)
