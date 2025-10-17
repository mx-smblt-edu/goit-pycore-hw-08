"""
Provides a function to display a contact's phone number.
"""
from decorators.input_error_decorator import input_error
from error.contact_not_found_error import ContactNotFoundError
from error.invalid_command_args_error import InvalidCommandArgsError
from model.address_book import AddressBook


@input_error
def show_phone(args: list[str], book: AddressBook) -> str:
    """
    Displays phone numbers associated with a contact's name from the address book.

    This function retrieves and returns the phone numbers linked to a specific
    contact name in the provided address book. If no numbers are found for the
    contact, or the contact does not exist, appropriate error handling is triggered.

    :param args: A list of arguments where the first element is the contact name.
    :param book: The AddressBook instance to search the contact in.
    :return: A formatted string listing the contact's phone numbers or a
             message indicating no numbers are found.

    :raises InvalidCommandArgsError: If the number of arguments provided is not
                                      exactly one.
    :raises ContactNotFoundError: If the contact with the specified name is not
                                  found in the address book.
    """
    if len(args) != 1:
        raise InvalidCommandArgsError("phone [name]")
    name = args[0]
    record = book.find(name)
    if record is None:
        raise ContactNotFoundError()

    if record.phones:
        return f"Phones: {"; ".join([f"{phone}" for phone in record.phones])}"

    return "No phones found."
