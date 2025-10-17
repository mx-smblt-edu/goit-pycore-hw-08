"""
Provides the Birthday class.
"""
from datetime import datetime

from error.invalid_birthday_error import InvalidBirthdayError
from model.field import Field


class Birthday(Field):
    """
    Represents a birthday field.

    This class provides functionality to store and handle a birthday
    date in a specific format. It ensures that the provided date string
    adheres to the expected format and converts it to a date object for
    further use.
    """
    format = "%d.%m.%Y"

    def __init__(self, value: str):
        try:
            date = datetime.strptime(value, Birthday.format).date()
            super().__init__(date)
        except ValueError:
            raise InvalidBirthdayError(value)

    def __str__(self) -> str:
        return f"Birthday: {self.value.strftime(Birthday.format)}"
