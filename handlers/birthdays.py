from decorators.input_error_decorator import input_error
from model.AddressBook import AddressBook


@input_error
def birthdays(book: AddressBook) -> str:
    upcoming_birthdays = book.get_upcoming_birthdays()
    if upcoming_birthdays:
        return "\n".join([f"Contact name: {item[0]}, birthday: {item[1]}" for item in upcoming_birthdays])
    else:
        return "No upcoming birthdays found."
