"""
A command-line virtual assistant bot for managing contacts and birthdays.

This module provides an interactive assistant that allows users to manage an
address book with functionalities such as adding and modifying contacts,
showing contact details, adding birthdays, and querying upcoming birthdays.
The assistant parses user input commands and executes corresponding actions
to interact with the AddressBook.
"""
from colorama import Fore, Style
from handlers.add_birthday import add_birthday
from handlers.add_contact import add_contact
from handlers.birthdays import birthdays
from handlers.change_contact import change_contact
from handlers.show_all import show_all
from handlers.show_birthday import show_birthday
from handlers.show_phone import show_phone
from model.AddressBook import AddressBook
from persistent import load_data, save_data


def parse_input(user_input: str) -> tuple[str, list[str]]:
    """
    Parses a user input string into a command and its arguments.

    This function processes a given input string, splits it into separate parts,
    and extracts the first element as the command while the remaining elements are
    treated as arguments. If the input is empty, it returns an empty command and
    an empty list of arguments.

    :param user_input: The raw input string to be parsed.
    :return: A tuple containing the extracted command and a list of its arguments.
    """
    parts = user_input.split()
    if not parts:
        return "", []
    cmd = parts[0].strip().lower()
    args = parts[1:]
    return cmd, args


def main():
    """
    Main function of the assistant bot application. This function serves as the entry
    point to the program and performs the following tasks:
    1. Loads the address book data.
    2. Provides a user interface to interact with the assistant bot via commands.
    3. Handles various user commands such as adding contacts, changing contact details,
       retrieving phone numbers, showing all contacts, managing birthdays, and
       exiting the application.
    4. Saves the address book data before exiting.

    The assistant bot utilizes a command-based interface, and the available commands
    include "hello", "add", "change", "phone", "all", "add-birthday", "show-birthday",
    "birthdays", and exit commands ("close", "exit"). Each command has its
    corresponding operation as defined in the function logic.

    :raises ValueError: If invalid input or command is provided.
    """
    book: AddressBook = load_data()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command == "":
            continue
        elif command in ["close", "exit"]:
            save_data(book)
            print(f"{Fore.BLUE}Good bye!{Style.RESET_ALL}")
            break
        elif command == "hello":
            print(f"{Fore.BLUE}How can I help you?{Style.RESET_ALL}")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(show_phone(args, book))
        elif command == "all":
            print(show_all(book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(birthdays(book))
        else:
            print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} Invalid command.")


if __name__ == "__main__":
    main()
