import json

from models import User
from src.controller.cors import response
from src.validators import UpdateUserModel


def update_user_main(event, context):
    response_body = {}
    try:
        data = json.loads(event["body"])
        UpdateUserModel(**data)
        user_id = data.pop("id", None)
        if user_id is not None:
            # * List of attributes of model schema_fields, which are not required for update operations
            NOT_REQUIRED = ["id", "creation_date", "_cls"]
            schema_fields = [k for k, v in User._fields.items() if k not in NOT_REQUIRED]

            # * key value pairs of updated attributes
            data_update = {i: data[i] for i in data if i in schema_fields and data[i] is not None}

            # * Update given parameters in respective Collection
            user = User.objects.get(id=user_id)
            user.update(**data_update)
            user.reload()

            response_body["data"] = json.loads(user.to_json())
            response_body["msg"] = "User updated successfully"
            response_body["status"] = True
        else:
            response_body["msg"] = "User Id should pass for update operation"
            response_body["status"] = False
        status_code = 200
    except Exception as e:
        response_body["msg"] = str(e)
        response_body["status"] = False
        status_code = 400
    return response(status_code, response_body)
