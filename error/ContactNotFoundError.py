"""
A module defining a custom exception to handle missing contacts.

This module provides a custom exception class `ContactNotFoundError` to
signal cases where a specific contact could not be located during an
operation.
"""
from colorama import Fore, Style


class ContactNotFoundError(Exception):
    """
    Represents an exception raised when a contact is not found.

    This custom exception is utilized to signal that a specific contact
    could not be located during an operation. It contains a predefined
    error message explaining the issue.
    """

    def __init__(self):
        self.message = f"{Fore.RED}[ERROR]{Style.RESET_ALL} Contact not found."
