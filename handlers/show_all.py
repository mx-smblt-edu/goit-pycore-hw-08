"""
Provides a function to display all contacts in an AddressBook.
"""
from model.address_book import AddressBook


def show_all(book: AddressBook) -> str:
    """
    Generates a string representation of all records in the provided
    `AddressBook`. If the `AddressBook` is empty, returns a message indicating
    that no contacts are found.

    :param book: An AddressBook instance containing contact records.
    :return: A string representation of all contact records or a message
        if no contacts are found.
    """
    if book:
        return "\n".join([f"{record}" for _, record in book.items()])

    return "No contacts found."
