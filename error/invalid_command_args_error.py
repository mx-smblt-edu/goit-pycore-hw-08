"""
This module defines an exception for handling invalid command argument errors.

The exception provides a custom error message formatted with color codes
to indicate the error and expected command format.
"""
from colorama import Fore, Style


class InvalidCommandArgsError(Exception):
    """
    Exception raised for errors in the number of arguments passed to a command.

    This exception is specifically intended to handle cases where the provided
    arguments to a command do not match the expected command format. It provides
    a clear error message highlighting the incorrect number of arguments and the
    expected command usage.

    :param command_format: The expected command format.
    """

    def __init__(self, command_format: str):
        self.message = (f"{Fore.RED}[ERROR]{Style.RESET_ALL} Invalid number of arguments.\n"
                        f"Expected the command format: {Fore.GREEN}{command_format}{Style.RESET_ALL}")
