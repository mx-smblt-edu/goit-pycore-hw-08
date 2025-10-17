"""
Provides a function to add or update a birthday for a contact in an AddressBook.
"""
from decorators.input_error_decorator import input_error
from error.invalid_command_args_error import InvalidCommandArgsError
from model.address_book import AddressBook
from model.record import Record


@input_error
def add_birthday(args: list[str], book: AddressBook) -> str:
    """
    Adds or updates a birthday for a contact within the address book.

    If the contact does not exist in the address book, it creates a new record
    with the specified name and birthday and adds it to the address book.
    If the contact already exists, it updates the existing record with the
    new birthday.

    :param args: A list containing exactly 2 elements: the name of the contact
        and their date of birth.
    :param book: The address book in which the contact's birthday
        will be added or updated.
    :return: A message confirming whether the birthday was added as a new contact
        or updated for an existing contact.
    :raises InvalidCommandArgsError: If the number of arguments provided is not 2.
    """
    if len(args) != 2:
        raise InvalidCommandArgsError("add-birthday [name] [date of birth]")
    name, birthday = args
    record = book.find(name)
    if record is None:
        record = Record(name)
        record.add_birthday(birthday)
        book.add_record(record)
        return "Birthday added to contact."

    record.add_birthday(birthday)
    return "Birthday updated in contact."
