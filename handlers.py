from decorators import input_error
from classes import Record
from datetime import datetime

@input_error
def add_contact(args, book):
    name, phone = args
    find_name = book.find(name)
    
    if not find_name :
        new_record = Record(name)
        new_record.add_phone(phone) 
        book.add_record(new_record)
        
        return f"Contact {name} added."
    else:
        find_name.add_phone(phone)
        return f"Phone added to contact {name}."

@input_error
def remove_phone(args,book):
    name,phone = args
    find_name = book.find(name)
    
    if find_name:
        find_name.remove_phone(phone)
    
        return f"{phone} is deleted"
    else:
        return f"Can't find {phone} in phonebook"    

@input_error
def change_contact(args, book):
    name, old_phone,new_phone = args
    contact = book.find(name)
   
    if contact:
        contact.edit_phone(old_phone,new_phone)
        return "Contact changed."
    else:
        return "Conctact not exist"
    
@input_error
def show_phone(args, book):
    name = args[0]
    contact = book.find(name)
   
    if contact:
        return contact

    else:
        return "Conctact not exist"

@input_error
def find_phone(args,book):
    name,phone = args

    contact = book.find(name)
    if contact:
        found_phone=contact.find_phone(phone)
        if found_phone:
            return found_phone
        else:
            return "phone not found"

    else:
        return "Conctact not exist"
    
    
@input_error
def show_all(book):
    
    for name, record in book.data.items():
         
       yield record


@input_error
def add_birthday(args, book):
    name,date = args
    contact=book.find(name)
    
    if contact:  
        contact.add_birthday(date)
        return "B-day Added"
    
    else:
        return "Conctact not exist"


@input_error
def show_birthday(args, book):
    name = args[0]
    
    contact=book.find(name)
    
    if contact:
        b_day=contact.show_birthday(name)
        if b_day:
            return b_day
        return "Please add b-day for contact"
    else:
        return "Conctact not exist"
    
@input_error
def birthdays(book):
    
    for name, record in book.data.items():
        contact = book.find(name)
        congrats = contact.birthdays(name)
        if not congrats:
            return 'No one to congratulate next week' 
        
        else:
            yield congrats
        
@input_error
def delete_contact(args,book):
    name=args[0]
    
    contact = book.find(name)
    if contact:
        book.delete(name)
        return f"Contact {name} deleted"
    else:
        return f"Contact {name} don't exist" 
        

# add Alex 1234569879
# add-birthday Alex 26.02.1990
# show-birthday Alex
# birthdays