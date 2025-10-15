from decorators.input_error_decorator import input_error
from error.ContactNotFoundError import ContactNotFoundError
from error.InvalidCommandArgsError import InvalidCommandArgsError
from model.AddressBook import AddressBook


@input_error
def show_birthday(args: list[str], book: AddressBook) -> str:
    if len(args) != 1:
        raise InvalidCommandArgsError("show-birthday [name]")
    name = args[0]
    record = book.find(name)
    if record is None:
        raise ContactNotFoundError()

    if record.birthday:
        return str(record.birthday)
    else:
        return "No birthday found."
