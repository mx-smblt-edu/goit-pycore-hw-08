"""
A decorator module for handling specific exceptions.

This module provides a decorator, `input_error`, to simplify error handling in
functions. It catches specific exceptions and returns their associated error messages
to the caller.
"""
from functools import wraps

from error.contact_not_found_error import ContactNotFoundError
from error.invalid_birthday_error import InvalidBirthdayError
from error.invalid_command_args_error import InvalidCommandArgsError
from error.invalid_phone_number_error import InvalidPhoneNumberError


def input_error(func):
    """
    Wraps a function to handle specific errors and return their associated error messages.

    This decorator is intended to simplify error handling within decorated functions by
    catching specific exceptions and returning their predefined messages to the caller.

    :param func: The function to be wrapped by the decorator.
    :type func: Callable
    :return: The wrapped function capable of handling specific exceptions and returning
             their associated messages.
    :rtype: Callable
    """

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
