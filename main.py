from handlers.add_birthday import add_birthday
from handlers.add_contact import add_contact
from handlers.birthdays import birthdays
from handlers.change_contact import change_contact
from handlers.show_all import show_all
from handlers.show_birthday import show_birthday
from handlers.show_phone import show_phone
from model.AddressBook import AddressBook
from colorama import Fore, Style


def parse_input(user_input: str) -> tuple[str, list[str]]:
    parts = user_input.split()
    if not parts:
        return "", []
    cmd = parts[0].strip().lower()
    args = parts[1:]
    return cmd, args


def main():
    book: AddressBook = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command == "":
            continue
        elif command in ["close", "exit"]:
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
