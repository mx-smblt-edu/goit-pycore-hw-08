"""
Provides a function to change a contact's phone number.
"""
from decorators.input_error_decorator import input_error
from error.ContactNotFoundError import ContactNotFoundError
from error.InvalidCommandArgsError import InvalidCommandArgsError
from model.AddressBook import AddressBook


@input_error
def change_contact(args: list[str], book: AddressBook) -> str:
    """
    Change the phone number for an existing contact in the address book. This function finds the
    record for a given contact name and updates their phone number from the specified old value
    to the new value.

    :param args: List containing exactly three elements: the contact's name (str), the old phone
        number to be replaced (str), and the new phone number to be set (str).
    :param book: The AddressBook instance where the contact's information is stored.
    :return: A confirmation message indicating that the contact's phone number has been updated.

    :raises InvalidCommandArgsError: If the number of arguments provided in `args` is not three.
    :raises ContactNotFoundError: If the contact with the specified name does not exist in the
        address book.
    """
    if len(args) != 3:
        raise InvalidCommandArgsError("change [name] [old phone number] [new phone number]")
    name, old_phone, new_phone = args

    record = book.find(name)
    if record is None:
        raise ContactNotFoundError()

    record.edit_phone(old_phone, new_phone)
    return "Contact updated."
