from decorators.input_error_decorator import input_error
from error.InvalidCommandArgsError import InvalidCommandArgsError
from model.AddressBook import AddressBook
from model.Record import Record


@input_error
def add_contact(args: list[str], book: AddressBook) -> str:
    if len(args) != 2:
        raise InvalidCommandArgsError("add [name] [phone number]")
    name, phone = args
    record = book.find(name)
    if record is None:
        record = Record(name)
        record.add_phone(phone)
        book.add_record(record)
        return "Contact added."
    else:
        record.add_phone(phone)
        return "Contact updated."
