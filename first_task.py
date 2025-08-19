from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        if not value or not value.strip():
            raise ValueError("The name is not valid. Write the correct one")
        super().__init__(value)
    

class Phone(Field):
    def __init__(self, value):
        if not self.is_valid_phone(value):
            raise ValueError("The phone number is in wrong format")
        super().__init__(value)
    
    #To check if the phone number was provided in correct format    
    def is_valid_phone(self, phone):
            return len(phone) == 10 and phone.isdigit()
            

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        phone_number = Phone(phone)
        self.phones.append(phone_number)

    def find_phone(self, phone):
        for number in self.phones:
            if number.value == phone:
                return number
        return None
    
    def remove_phone(self, phone):
        phone_obj = self.find_phone(phone)
        if phone_obj:
            self.phones.remove(phone_obj)
            return phone_obj
        return None
                
    def edit_phone(self, phone, new_phone):
        new_phone_number = Phone(new_phone)
        if self.find_phone(phone):
            self.remove_phone(phone)
            self.add_phone(new_phone)
        else:
            raise ValueError("Phone number is missing")
        

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '. join(p.value for p in self.phones)}"
    

class AddressBook(UserDict):
         
    def add_record(self, record):
        self.data[record.name.value] = record
     
    def find(self, name):
        return self.data.get(name)
    
    def delete(self, name):
        if name in self.data:
            del self.data[name]
    
    def __str__(self):
        if not self.data:
            return "Address book is empty"
        
        result = []
        for record in self.data.values():
            result.append(str(record))
        return "\n".join(result)

    
# Test the implementation
book = AddressBook()

john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

book.add_record(john_record)

jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

print(book)

john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)

found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")

book.delete("Jane")



