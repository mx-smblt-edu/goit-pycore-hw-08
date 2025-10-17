"""
Provides an AddressBook class for managing and storing contact information.
"""
from collections import UserDict
from datetime import timedelta, datetime, date

from model.birthday import Birthday
from model.record import Record


class AddressBook(UserDict[str, Record]):
    """A class for storing and managing records."""

    def add_record(self, record: Record) -> None:
        """
        Add a record to the data storage.

        This method adds a record to the internal data storage only if the record's key
        does not already exist in the storage. The key is determined using the record's
        name attribute.

        :param record: The record to be added to the data storage
        :return: None
        """
        key = record.name.value
        if key not in self.data:
            self.data[key] = record

    def find(self, name: str) -> Record | None:
        """
        Searches for a record by its name in the data mapping.

        This method attempts to retrieve a record from the internal data mapping.
        If the name exists in the mapping, the corresponding record is returned.
        If the name does not exist, `None` is returned.

        :param name: The name of the record to search for.
        :return: The associated record if found, otherwise `None`.
        """
        return self.data.get(name, None)

    def delete(self, name: str) -> Record | None:
        """
        Deletes a record from the internal data storage by its name. If the record
        with the given name exists, it will be removed and returned. Otherwise,
        returns None.

        :param name: The name of the record to be deleted.
        :returns: The deleted record if it existed; otherwise, None.
        """
        return self.data.pop(name, None)

    def get_upcoming_birthdays(self) -> list[tuple[str, str]]:
        """
        Get a list of upcoming birthdays within a 7-day range.

        This method retrieves a list of contacts whose birthdays fall within
        the next 7 days from the current date. The method accesses contact data,
        extracts birthdays, and determines if they occur in the specified range.
        The result contains tuples of contact names and their corresponding
        upcoming birthday dates in the desired format.

        :return: A list of tuples where each tuple contains the contact name and the
            upcoming birthday's formatted date.
        """
        contacts: dict[str, Record] = self.data
        start_date = datetime.today().date()
        end_date = start_date + timedelta(days=7)

        result: list[tuple[str, str]] = []
        for _, record in contacts.items():
            birthday = record.birthday
            if birthday is None:
                continue

            congratulation_date = AddressBook.__get_congratulation_date(birthday, start_date, end_date)
            if congratulation_date:
                result.append((record.name.value, congratulation_date.strftime(Birthday.format)))

        return result

    @staticmethod
    def __get_congratulation_date(birthday: Birthday, start_date: date, end_date: date) -> date | None:
        """
        Determines the appropriate congratulation date for a given birthday, ensuring it falls
        within the specified start and end date period. If the estimated birthday is on a weekend
        (Saturday or Sunday), the method adjusts the congratulation date to the following Monday.

        :param birthday: The person's birthday information
        :param start_date: The start date of the validation period
        :param end_date: The end date of the validation period
        :return: The date when the congratulation should take place or None if no suitable
                 date exists within the given range
        """
        estimated_birthday: date = birthday.value.replace(year=start_date.year)

        if estimated_birthday < start_date:
            estimated_birthday = estimated_birthday.replace(year=start_date.year + 1)

        if start_date <= estimated_birthday <= end_date:
            day_of_week = estimated_birthday.weekday()
            if day_of_week == 6:  # birthday on Sunday
                congratulation_date = estimated_birthday + timedelta(days=1)
            elif day_of_week == 5:  # birthday on Saturday
                congratulation_date = estimated_birthday + timedelta(days=2)
            else:
                congratulation_date = estimated_birthday
            return congratulation_date

        return None

    def __str__(self) -> str:
        return "AddressBook\n" + '\n'.join([f'{record}' for record in self.data.values()])
