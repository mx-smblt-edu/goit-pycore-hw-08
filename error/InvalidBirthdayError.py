from colorama import Fore, Style


class InvalidBirthdayError(Exception):
    def __init__(self, date: str):
        self.message = f"{Fore.RED}[ERROR]{Style.RESET_ALL} Invalid date format '{date}'. Use {Fore.GREEN}DD.MM.YYYY{Style.RESET_ALL}."
