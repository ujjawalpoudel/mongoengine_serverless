import re
import pydantic
from typing import List, Optional

from src.utils.exception_handle import EmailValidationError, PhoneNumberValidationError


class UserModel(pydantic.BaseModel):
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
            raise EmailValidationError(email=email, message=message)

    @pydantic.validator("phone")
    @classmethod
    def phone_valid_check(cls, phone) -> None:
        #* Make a regular expression for validating Phone Number
        regex = r'^(?:[+977]9)?[0-9]{10}$'
        if(re.fullmatch(regex, phone)):
            return phone
        else:
            message = "Given phone number ({0}) is not valid.".format(phone)
            raise PhoneNumberValidationError(phone=phone, message=message)
