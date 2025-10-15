from functools import wraps

from error.ContactNotFoundError import ContactNotFoundError
from error.InvalidBirthdayError import InvalidBirthdayError
from error.InvalidCommandArgsError import InvalidCommandArgsError
from error.InvalidPhoneNumberError import InvalidPhoneNumberError


def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ContactNotFoundError as e:
            return e.message
        except InvalidCommandArgsError as e:
            return e.message
        except InvalidPhoneNumberError as e:
            return e.message
        except InvalidBirthdayError as e:
            return e.message

    return inner
