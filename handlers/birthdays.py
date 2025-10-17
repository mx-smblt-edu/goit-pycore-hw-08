"""
Provides a function to retrieve and format upcoming birthdays from an AddressBook.
"""
from decorators.input_error_decorator import input_error
from model.address_book import AddressBook


@input_error
def birthdays(book: AddressBook) -> str:
    """
    Retrieves upcoming birthdays from the provided AddressBook and formats the information.

    :param book: AddressBook instance containing contact details and
        birthday information.
    :return: Formatted string with names and birthdays of contacts who
        have upcoming birthdays or a message indicating no upcoming
        birthdays.
    """
    upcoming_birthdays = book.get_upcoming_birthdays()
    if upcoming_birthdays:
        return "\n".join([f"Contact name: {item[0]}, birthday: {item[1]}" for item in upcoming_birthdays])
    else:
        return "No upcoming birthdays found."
