from abc import ABC, abstractmethod

import handlers
import data


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


class Bot(ABC):
    @abstractmethod
    def display_command(self, commands):
        pass

    @abstractmethod
    def display_contacts(self, contacts):
        pass


class ConsoleBot(Bot):
    def display_command(self, commands):
        print("Available commands:")
        for command in commands:
            print(f"- {command}")

    def display_contacts(self, contacts):
        print("\n".join([str(contact) for contact in contacts]))


def main(ui):

    book = data.load_data()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(handlers.add_contact(args, book))
        elif command == "change":
            print(handlers.change_contact(args, book))
        elif command == "phone":
            print(handlers.show_phone(args, book))
        elif command == "find-phone":
            print(handlers.find_phone(args, book))
        elif command == "all":
            ui.display_contacts(book.data.values())
            # for result in handlers.show_all(book):
            #     print(result)
        elif command == "remove":
            print(handlers.remove_phone(args, book))
        elif command == "add-birthday":
            print(handlers.add_birthday(args, book))
        elif command == "show-birthday":
            print(handlers.show_birthday(args, book))
        elif command == "delete":
            print(handlers.delete_contact(args, book))
        elif command == "birthdays":
            for result in handlers.birthdays(book):
                print(result)

        elif command == "commands":
            ui.display_commands(
                [
                    "hello",
                    "add",
                    "change",
                    "phone",
                    "all",
                    "add-birthday",
                    "show-birthday",
                    "birthdays",
                    "close",
                    "exit",
                ]
            )

        else:
            print("Invalid command.")
    data.save_data(book)


if __name__ == "__main__":
    ui = ConsoleBot()
    main(ui)
