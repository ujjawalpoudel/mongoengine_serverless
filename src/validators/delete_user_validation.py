import pydantic
import bson

from src.utils.exception_handler import ValidationError


class DeleteUserModel(pydantic.BaseModel):
    id: str

    @pydantic.validator("id")
    @classmethod
    def id_valid_check(cls, id) -> None:
        #* Check mongo ObjectID is valid.
        if bson.objectid.ObjectId.is_valid(id):
            return id
        else:
            message = "Given id ({0}) is not valid object id.".format(id)
            raise ValidationError(value=id, message=message)
