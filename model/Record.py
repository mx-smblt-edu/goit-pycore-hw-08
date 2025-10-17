"""
Provides the Record class.
"""
from model.Birthday import Birthday
from model.Name import Name
from model.Phone import Phone


class Record:
    """A class for storing contact information, which contains a name and a list of phones."""

    def __init__(self, name: str):
        self.name = Name(name)
        self.phones: list[Phone] = []
        self.birthday = None

    def add_phone(self, phone_number: str) -> Phone | None:
        """
        Adds a phone number to the list if it is not already present.

        :param phone_number: The phone number to be added.
        :return: A new Phone object if the phone number is successfully added,
            or None if the phone number is already present in the list.
        """
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
        """
        Edits an existing phone number in the phone list. Replaces the old phone number
        with a new one if the old number exists and the new number is not already in use.

        :param old_phone_number: The phone number currently stored in the list that
            needs to be replaced.
        :param new_phone_number: The new phone number to replace the old one. Must not
            already exist in the list.
        :return: The newly created Phone object representing the new phone number.
        :raises ValueError: If the old phone number is not found in the list.
        :raises ValueError: If the new phone number is already in the list.
        """
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
        """
        Removes a phone number from the stored phone list, if it exists.

        Searches for the specified phone number in the list of stored phones. If the
        phone number is found, it is removed from the list and returned. If the phone
        number is not found, no operation is performed, and None is returned.

        :param phone_number: The phone number to be removed.
        :return: The removed phone instance if the phone number exists, otherwise None.
        """
        index_phone_number = self.__index_phone_number(phone_number)
        if index_phone_number is not None:
            # Номер телефону є у списку
            return self.phones.pop(index_phone_number)
        else:
            # Номер телефону відсутній у списку
            return None

    def find_phone(self, phone_number: str) -> Phone | None:
        """
        Finds a phone from a list using the provided phone number.

        This method searches for the given phone number in the internal list of
        phones by indexing it. If the phone number exists in the list, it returns
        the corresponding phone object. If the phone number is not found, it
        returns None.

        :param phone_number: The phone number to search for.
        :return: The phone object if found, otherwise None.
        """
        index_phone_number = self.__index_phone_number(phone_number)
        if index_phone_number is not None:
            # Номер телефону є у списку
            return self.phones[index_phone_number]
        else:
            # Номер телефону відсутній у списку
            return None

    def add_birthday(self, birthday: str) -> Birthday:
        """
        Adds a birthday to the instance and returns the Birthday object.

        :param birthday: A string representing the birthday to be added.
        :return: The Birthday object created from the supplied string.
        """
        self.birthday = Birthday(birthday)
        return self.birthday

    def __index_phone_number(self, phone_number: str) -> int | None:
        """
        Searches for the index of a phone number in the list of stored phone numbers.

        This method iterates through the list of phone numbers and checks if any of the
        numbers matches the provided phone number. If a match is found, the index of the
        phone number in the list is returned. If no match is found, the method returns None.

        :param phone_number: The phone number to search for in the list.
        :return: The index of the phone number if found, or None if no match is found.
        """
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
