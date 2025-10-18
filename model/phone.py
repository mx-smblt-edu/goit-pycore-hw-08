"""
Provides the Phone class.
"""
import re

from error.invalid_phone_number_error import InvalidPhoneNumberError
from model.field import Field


class Phone(Field):
    """Class for storing phone numbers. Has format validation (10 digits)"""

    __pattern: re.Pattern = re.compile(r"^\d{10}$")

    def __init__(self, number: str):
        if re.fullmatch(Phone.__pattern, number) is None:
            raise InvalidPhoneNumberError(number)
        super().__init__(number)
