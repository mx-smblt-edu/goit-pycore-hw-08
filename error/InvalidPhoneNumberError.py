from colorama import Fore, Style


class InvalidPhoneNumberError(Exception):
    def __init__(self, phone_number: str):
        self.message = f"{Fore.RED}[ERROR]{Style.RESET_ALL} Invalid phone number: '{phone_number}'."
