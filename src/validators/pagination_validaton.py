import re
import pydantic
from typing import List, Optional

from src.utils.exception_handle import PaginationValidationError


class PaginationModel(pydantic.BaseModel):
    page_size: Optional[str]
    page_num: Optional[str]

    @pydantic.validator("page_size")
    @classmethod
    def page_size_valid_check(cls, page_size):
        try:
            return int(page_size)
        except ValueError:
            message = "Given page_size ({0}) is not valid integer.".format(page_size)
            raise PaginationValidationError(item=page_size, message=message)

    @pydantic.validator("page_num")
    @classmethod
    def page_num_valid_check(cls, page_num):
        try:
            return int(page_num)
        except ValueError:
            message = "Given page_num ({0}) is not valid integer.".format(page_num)
            raise PaginationValidationError(item=page_num, message=message)
