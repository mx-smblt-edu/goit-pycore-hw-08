from decorators.input_error_decorator import input_error
from error.ContactNotFoundError import ContactNotFoundError
from error.InvalidCommandArgsError import InvalidCommandArgsError
from model.AddressBook import AddressBook


@input_error
def change_contact(args: list[str], book: AddressBook) -> str:
    if len(args) != 3:
        raise InvalidCommandArgsError("change [name] [old phone number] [new phone number]")
    name, old_phone, new_phone = args

    record = book.find(name)
    if record is None:
        raise ContactNotFoundError()

    record.edit_phone(old_phone, new_phone)
    return "Contact updated."
