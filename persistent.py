import pickle

from model.AddressBook import AddressBook

__file_name = "address-book.db"


def save_data(book: AddressBook, filename: str = __file_name):
    with open(filename, "wb") as file:
        pickle.dump(book, file)


def load_data(filename: str = __file_name) -> AddressBook:
    try:
        with open(filename, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return AddressBook()
