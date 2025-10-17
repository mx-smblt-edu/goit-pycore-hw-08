"""
Provides functions to save and load AddressBook objects.
"""
import pickle

from model.address_book import AddressBook

__DEFAULT_FILE_NAME = "address-book.db"


def save_data(book: AddressBook, filename: str = __DEFAULT_FILE_NAME) -> None:
    """
    Saves the given AddressBook instance to a file using Python's pickle module.

    This function serializes the AddressBook object and writes it to a file in
    binary format. The specified filename is used as the target file. By default,
    if the filename is not provided, a predefined system default is used.

    :param book: The AddressBook instance containing contact data
        that needs to be serialized and stored.
    :param filename: The name of the file where the data will be
        saved. Defaults to the predefined system default filepath.
    :return: None
    """
    with open(filename, "wb") as file:
        pickle.dump(book, file)


def load_data(filename: str = __DEFAULT_FILE_NAME) -> AddressBook:
    """
    Loads data from a file and returns an AddressBook instance. If the file is not found, an empty
    AddressBook is returned. The function utilizes Python's pickle module for serialization
    and deserialization.

    :param filename: The path to the file from which data will be loaded.
    :return: An AddressBook instance containing the loaded data, or a new empty AddressBook
             if the file does not exist.
    """
    try:
        with open(filename, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return AddressBook()
