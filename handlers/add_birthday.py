from decorators.input_error_decorator import input_error
from error.InvalidCommandArgsError import InvalidCommandArgsError
from model.AddressBook import AddressBook
from model.Record import Record


@input_error
def add_birthday(args: list[str], book: AddressBook) -> str:
    if len(args) != 2:
        raise InvalidCommandArgsError("add-birthday [name] [date of birth]")
    name, birthday = args
    record = book.find(name)
    if record is None:
        record = Record(name)
        record.add_birthday(birthday)
        book.add_record(record)
        return "Birthday added to contact."
    else:
        record.add_birthday(birthday)
        return "Birthday updated in contact."
