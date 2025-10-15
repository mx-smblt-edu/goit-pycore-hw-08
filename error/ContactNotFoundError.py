from colorama import Fore, Style


class ContactNotFoundError(Exception):
    def __init__(self):
        self.message = f"{Fore.RED}[ERROR]{Style.RESET_ALL} Contact not found."
