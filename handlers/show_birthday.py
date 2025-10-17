"""
Provides a function to display a contact's birthday.
"""
from decorators.input_error_decorator import input_error
from error.ContactNotFoundError import ContactNotFoundError
from error.InvalidCommandArgsError import InvalidCommandArgsError
from model.AddressBook import AddressBook


@input_error
def show_birthday(args: list[str], book: AddressBook) -> str:
    """
    Shows the birthday of a contact by name. If the contact exists and a birthday
    is recorded in the address book, it returns the birthday. Otherwise, it
    returns a message indicating no birthday is found.

    :param args: The list of arguments, where the first element should be the name
        of the contact as a string.
    :param book: The address book instance where the contact's information is
        stored.
    :return: The birthday as a string if found, or a message indicating no
        birthday is available.
    :raises InvalidCommandArgsError: Raised if the number of arguments passed does
        not match the required format or is invalid.
    :raises ContactNotFoundError: Raised if the specified name cannot be found in
        the address book.
    """
    if len(args) != 1:
        raise InvalidCommandArgsError("show-birthday [name]")
    name = args[0]
    record = book.find(name)
    if record is None:
        raise ContactNotFoundError()

    if record.birthday:
        return str(record.birthday)
    else:
        return "No birthday found."
