import re
import pydantic
import bson
from typing import List, Optional

from src.utils.exception_handler import ValidationError


class UpdateUserModel(pydantic.BaseModel):
    id: str
    name: Optional[str]
    age: Optional[int]
    email: Optional[str]
    phone: Optional[str]
    address: Optional[str]

    @pydantic.validator("email")
    @classmethod
    def email_valid_check(cls, email) -> None:
        #* Make a regular expression for validating an Email
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if(re.fullmatch(regex, email)):
            return email
        else:
            message = "Given email address ({0}) is not valid.".format(email)
            raise ValidationError(value=email, message=message)

    @pydantic.validator("phone")
    @classmethod
    def phone_valid_check(cls, phone) -> None:
        #* Make a regular expression for validating Phone Number
        regex = r'^(?:[+977]9)?[0-9]{10}$'
        if(re.fullmatch(regex, phone)):
            return phone
        else:
            message = "Given phone number ({0}) is not valid.".format(phone)
            raise ValidationError(value=phone, message=message)

    @pydantic.validator("id")
    @classmethod
    def id_valid_check(cls, id) -> None:
        #* Check mongo ObjectID is valid.
        if bson.objectid.ObjectId.is_valid(id):
            return id
        else:
            message = "Given id ({0}) is not valid object id in update operation.".format(id)
            raise ValidationError(value=id, message=message)
