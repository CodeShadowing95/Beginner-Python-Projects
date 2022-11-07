import os
os.chdir(r"C:/Users/ukisu\Documents/Beginner-Projects-Python/Contact Book")


class Person:
    # Defining constructor
    def __init__(self, name):
        self.name = name
    

class Contact(Person):
    def __init__(self, contact_name=None, address=None, phone_number=None, email=None):
        super().__init__(contact_name)
        self.address = address
        self.phone_number = phone_number
        self.email = email
    
    def listContacts(self):
        datas = []
        with open("MyContacts.txt", 'r+', encoding='utf-8') as fp:
            for line in fp:
                print(f"{line}")
                datas.append([line])
        return datas
    
    def addContact(self):
        with open('MyContacts.txt', 'a+', encoding='utf-8') as file_contacts:
            c = f"{self.name}, {self.address}, {self.phone_number}, {self.email}\n"
            file_contacts.write(c)
            print("Contact saved successfully!!!")
    
    def updateContact(self, oldValue, newValue):
        with open('MyContacts.txt', encoding='utf-8') as fp:
            # Store each line (with leading and trailing whitespaces removed) in list 
            datas = [line.strip() for line in fp.readlines()]
            for line in datas:
                if oldValue in line:
                    # Get the index of the line containig the old value
                    pos = datas.index(line)
                    # Get each line as a string, so we must convert the string into list, to access to the specific data
                    data = line.split(', ')
                    for i in range(len(data)):
                        # If the data contains spaces and the old value
                        if " " in data[i] and oldValue in data[i]:
                            d = data[i].split(" ")
                            for j in range(len(d)):
                                if oldValue in d[j]:
                                    d[j] = newValue
                                    data[i] = " ".join(d)
                                    line = ", ".join(data)
                                    datas[pos] = line
                                    with open('MyContacts.txt', 'w', encoding="utf-8") as fp:
                                        for line in datas:
                                            fp.write(line + '\n')
                                    return True
                        # If it doesn't contain any spaces and the value is there
                        elif oldValue == data[i]:
                            data[i] = newValue
                            line = ", ".join(data)
                            datas[pos] = line
                            with open('MyContacts.txt', 'w', encoding="utf-8") as fp:
                                for line in datas:
                                    fp.write(line + '\n')
                            return True
            if oldValue not in [x for x in datas]:
                return False
    
    def deleteContact(self, contact):
        with open("MyContacts.txt", 'r', encoding='utf-8') as fp:
            contacts = fp.readlines()
            for line in contacts:
                if contact in line:
                    contacts.remove(line)
                    with open("MyContacts.txt", "w", encoding='utf-8') as fp:
                        for line in contacts:
                            fp.write(line)
                        return True
                    
                
        
            


def add_new_contact():
    while 1:
        os.system("cls")
        fname = input("Enter the contact name: ")
        address = input("Enter the contact address: ")
        phoneNumber = input("Enter the phone number: ")
        email = input("Enter the contact email: ")

        c = Contact(fname, address, phoneNumber, email)
        c.addContact()
        
        e = input("Create a new contact ? (y/n) ")
        if e in ('y', 'Y', 'Yes', 'yes'):
            continue
        elif e in ('n', 'N', 'No', 'no'):
            break


def update_contact():
    os.system('cls')
    c = Contact()
    c.listContacts()
    old_value = input("\nWhich data you'd like to update? ")
    new_value = input("Enter the data: ")
    found = c.updateContact(old_value, new_value)
    if found:
        print("Contact updated successfully!!!\n")
        c.listContacts()
    else:
        print("Contact not found!!!")
    

def delete_contact():
    os.system("cls")
    c = Contact()
    c.listContacts()
    val = input("Which contact do you want to delete ? ")
    found = c.deleteContact(val)
    if found:
        print("Contact deleted!!!")
    else:
        print("Contact not found!!!")


def list_contacts():
    os.system("cls")
    c = Contact()
    c.listContacts()
    


print("1. Add a new contact")
print("2. Update a contact")
print("3. Delete a contact")
print("4. List all contacts")
p = input("Choose an option: ")
if p == '1' or p == 1:
    add_new_contact()
if p == '2' or p == 2:
    update_contact()
if p == '3' or p == 3:
    delete_contact()
if p == '4' or p == 4:
    list_contacts()

