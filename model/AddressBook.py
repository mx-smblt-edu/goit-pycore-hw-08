from collections import UserDict
from datetime import timedelta, datetime, date
from model.Birthday import Birthday
from model.Record import Record


class AddressBook(UserDict[str, Record]):
    """Клас для зберігання та управління записами."""

    def add_record(self, record: Record):
        key = record.name.value
        if key not in self.data:
            self.data[key] = record

    def find(self, name: str) -> Record | None:
        return self.data.get(name, None)

    def delete(self, name: str) -> Record | None:
        return self.data.pop(name, None)

    def get_upcoming_birthdays(self) -> list[tuple[str, str]]:
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
        else:
            return None

    def __str__(self) -> str:
        return "AddressBook\n" + '\n'.join([f'{record}' for record in self.data.values()])
