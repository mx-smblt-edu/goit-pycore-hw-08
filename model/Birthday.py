from datetime import datetime
from error.InvalidBirthdayError import InvalidBirthdayError
from model.Field import Field


class Birthday(Field):
    format = "%d.%m.%Y"

    def __init__(self, value: str):
        try:
            date = datetime.strptime(value, Birthday.format).date()
            super().__init__(date)
        except ValueError:
            raise InvalidBirthdayError(value)

    def __str__(self) -> str:
        return f"Birthday: {self.value.strftime(Birthday.format)}"
