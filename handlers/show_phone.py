from decorators.input_error_decorator import input_error
from error.ContactNotFoundError import ContactNotFoundError
from error.InvalidCommandArgsError import InvalidCommandArgsError
from model.AddressBook import AddressBook


@input_error
def show_phone(args: list[str], book: AddressBook) -> str:
    if len(args) != 1:
        raise InvalidCommandArgsError("phone [name]")
    name = args[0]
    record = book.find(name)
    if record is None:
        raise ContactNotFoundError()

    if record.phones:
        return f"Phones: {"; ".join([f"{phone}" for phone in record.phones])}"
    else:
        return "No phones found."
