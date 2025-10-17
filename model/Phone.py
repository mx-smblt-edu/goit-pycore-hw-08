"""
Provides the Phone class.
"""
from error.InvalidPhoneNumberError import InvalidPhoneNumberError
from model.Field import Field
import re


class Phone(Field):
    """Class for storing phone numbers. Has format validation (10 digits)"""

    __pattern__: re.Pattern = re.compile(r"^\d{10}$")

    def __init__(self, number: str):
        if re.fullmatch(self.__pattern__, number) is None:
            raise InvalidPhoneNumberError(number)
        super().__init__(number)
