from colorama import Fore, Style


class InvalidCommandArgsError(Exception):
    def __init__(self, command_format: str):
        self.message = (f"{Fore.RED}[ERROR]{Style.RESET_ALL} Invalid number of arguments.\n"
                        f"Expected the command format: {Fore.GREEN}{command_format}{Style.RESET_ALL}")
