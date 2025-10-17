"""
Provides a function to add a contact to an AddressBook.
"""

from decorators.input_error_decorator import input_error
from error.invalid_command_args_error import InvalidCommandArgsError
from model.address_book import AddressBook
from model.record import Record


@input_error
def add_contact(args: list[str], book: AddressBook) -> str:
    """
    Adds a new contact or updates an existing contact by adding a phone number to the
    specified address book.

    This function takes a name and a phone number as arguments, checks if the name
    is already present in the address book, and performs one of the following actions:
    - If the name is not present, it creates a new contact and adds the specified phone
      number.
    - If the name already exists, it updates the existing contact by appending the new
      phone number to the list of phone numbers for that contact.

    :param args: A list containing exactly 2 elements: the name of the contact and the phone number.
    :param book: The address book in which the contact is to be added or updated.
    :raises InvalidCommandArgsError: If the number of arguments provided is not exactly two.
    :returns: A success message specifying whether the contact was added or updated.
    """
    if len(args) != 2:
        raise InvalidCommandArgsError("add [name] [phone number]")
    name, phone = args
    record = book.find(name)
    if record is None:
        record = Record(name)
        record.add_phone(phone)
        book.add_record(record)
        return "Contact added."

    record.add_phone(phone)
    return "Contact updated."
