from model.Birthday import Birthday
from model.Name import Name
from model.Phone import Phone


class Record:
    """Клас для зберігання інформації про контакт, який містить ім'я та список телефонів."""

    def __init__(self, name: str):
        self.name = Name(name)
        self.phones: list[Phone] = []
        self.birthday = None

    def add_phone(self, phone_number: str) -> Phone | None:
        index_phone_number = self.__index_phone_number(phone_number)
        if index_phone_number is None:
            # Номер телефону відсутній у списку
            phone = Phone(phone_number)
            self.phones.append(phone)
            return phone
        else:
            # Номер телефону вже мається у списку
            return None

    def edit_phone(self, old_phone_number: str, new_phone_number: str) -> Phone:
        index_old_phone_number = self.__index_phone_number(old_phone_number)
        if index_old_phone_number is None:
            # Старий номер телефону відсутній у списку
            raise ValueError(f"Phone '{old_phone_number}' is not found.")

        if self.__index_phone_number(new_phone_number) is not None:
            # Новий номер телефону вже є у списку
            raise ValueError(f"Phone '{new_phone_number}' is already used.")

        new_phone = Phone(new_phone_number)
        self.phones[index_old_phone_number] = new_phone
        return new_phone

    def remove_phone(self, phone_number: str) -> Phone | None:
        index_phone_number = self.__index_phone_number(phone_number)
        if index_phone_number is not None:
            # Номер телефону є у списку
            return self.phones.pop(index_phone_number)
        else:
            # Номер телефону відсутній у списку
            return None

    def find_phone(self, phone_number: str) -> Phone | None:
        index_phone_number = self.__index_phone_number(phone_number)
        if index_phone_number is not None:
            # Номер телефону є у списку
            return self.phones[index_phone_number]
        else:
            # Номер телефону відсутній у списку
            return None

    def add_birthday(self, birthday: str) -> Birthday:
        self.birthday = Birthday(birthday)
        return self.birthday

    def __index_phone_number(self, phone_number: str) -> int | None:
        """Повертає індекс номера телефону у списку або None."""
        for index, item in enumerate(self.phones):
            if item.value == phone_number:
                return index
        return None

    def __str__(self):
        result = f"Contact name: {self.name}"
        if self.birthday:
            result = result + f", birthday: {self.birthday.value.strftime(Birthday.format)}"
        if self.phones:
            result = result + f", phones: {'; '.join([f'{phone}' for phone in self.phones])}"
        return result
