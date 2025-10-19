"""
A module defining a custom exception for handling invalid birthday date formats.

This module provides an `InvalidBirthdayError` exception for scenarios where
a user provides a birthday date in an invalid format. The exception guides
the user to use the correct `DD.MM.YYYY` format.
"""
from colorama import Fore, Style


class InvalidBirthdayError(Exception):
    """
    Exception raised for invalid birthday date format.

    This exception is raised when a birthday date is provided in an invalid
    format. It informs the user to use the correct format `DD.MM.YYYY`.

    :param date: The invalid birthday date string.
    """

    def __init__(self, date: str):
        self.message = (f"{Fore.RED}[ERROR]{Style.RESET_ALL} Invalid date format '{date}'. "
                        f"Use {Fore.GREEN}DD.MM.YYYY{Style.RESET_ALL}.")
