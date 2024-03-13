from collections import UserDict
from datetime import datetime
from helpers import get_upcoming_birthdays


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):

    def __init__(self, value):
        if len(value) != 0:
            super().__init__(value)
        else:
            raise ValueError("Incorrect name")


class Phone(Field):
    def __init__(self, value):
        if len(value) == 10 and value.isdigit():
            super().__init__(value)
        else:
            raise ValueError("Incorrect phone format")


class Birthday(Field):
    def __init__(self, value):
        try:
            validDate = datetime.strptime(value, "%d.%m.%Y").date()

            super().__init__(validDate)

        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))  # додавання  телефона за допомогою класа Phone

    def remove_phone(self, phone):
        for el in self.phones:
            if el.value == phone:
                self.phones.remove(el)  # видалення телефону

    def edit_phone(self, old_phone, new_phone):

        Phone(new_phone)

        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone  # зміна номера

                break
        else:
            raise ValueError("Phone doesn't exist")

    def find_phone(self, phone):
        for el in self.phones:
            if el.value == phone:
                return el

    def add_birthday(self, b_day):
        self.birthday = Birthday(b_day)
        return self.birthday

    def show_birthday(self, name):
        if self.name.value == name:
            if self.birthday:
                return self.birthday.value.strftime("%d.%m.%Y")

    def birthdays(self, name):
        if self.name.value == name and self.birthday:
            user = {
                "name": self.name.value,
                "birthday": self.birthday.value.strftime("%d.%m.%Y"),
            }
            b_day = get_upcoming_birthdays(user)
            return b_day

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record  # додавання запису

    def find(self, name):
        return self.data.get(name)  # пошук запису

    def delete(self, name):
        if name in self.data:
            del self.data[name]
