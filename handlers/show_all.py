from model.AddressBook import AddressBook


def show_all(book: AddressBook) -> str:
    if book:
        return "\n".join([f"{record}" for _, record in book.items()])
    else:
        return "No contacts found."
