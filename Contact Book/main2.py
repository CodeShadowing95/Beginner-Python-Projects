import mysql.connector
import os
os.system('cls')


if __name__ == '__main__':
    
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "phone_book"
    )

    # Creating an instance of 'cursor' class which is used to execute SQL statements in Python
    cursor = mydb.cursor()
    
    # cursor.execute("""
    #     CREATE TABLE IF NOT EXISTS contact (
    #         firstname VARCHAR(255),
    #         lastname VARCHAR(255),
    #         phone_number int NOT NULL,
    #         email VARCHAR(255)
    #     );
    # """)
        
    print("1. Add a new contact")
    print("2. Update a contact")
    print("3. Delete a contact")
    print("4. List all contacts")
    entry = input("Choose an option: ")
    while type(entry) != int and int(entry) not in range(1, 5):
        entry = input("Enter only digits between 1 and 4 to choose an option: ")
    
    entry = int(entry)
    vals, i = [], 1
    if entry == 1:
        while 1:
            print("Contact ", i, "\n")
            firstname = input("First name: ")
            lastname = input("Last name: ")
            phone_number = int(input("Phone number: "))
            email_address = input("Email address: ")
            data = (firstname, lastname, phone_number, email_address)
            vals.append(data)
            
            c = input("Add a new contact ? (y/n) ")
            if c in ["n", "N", "no", "No", "NO"]:
                break
            i += 1
        
        sql_query = "INSERT INTO phone_book.contact (firstname, lastname, phone_number, email) VALUES(%s, %s, %s, %s)"
        cursor.executemany(sql_query, vals)
        mydb.commit()
        print(cursor.rowcount, " contacts added successfully!!!")
    # Update the contact
    elif entry == 2:
        os.system("cls")
        print("My current contacts:")
        cursor.execute("""SELECT firstname, lastname, phone_number, email FROM contact;""")
        rows = cursor.fetchall()
        for row in rows:
            print("{0} {1} - {2} - {3}\n".format(row[0], row[1], row[2], row[3]))
        
        getContact = input("Which contact you'd like to update? (Type only the phone number): ")
        
        cursor.execute("""SELECT firstname, lastname, phone_number, email FROM contact WHERE phone_number = %s""", (getContact, ))
        rows = cursor.fetchall()
        if len(rows) == 0:
            print("Contact not found!!!")
        else:
            datas = {"1": "firstname", "2": "lastname", "3": "phone_number", "4": "email"}
            tab, tab2 = {}, []
            for row in rows:
                print("{0} {1} - {2} - {3}".format(row[0], row[1], row[2], row[3]))
                print("What do you want to change about the contact information:")
                print("1. First name")
                print("2. Last name")
                print("3. Phone number")
                print("4. Email address")
                user_input = input("Choose the items (separated by commas): ")
                while user_input == "":
                    user_input = input("Choose the correct items (separated by commas): ")
                d = (user_input.replace(" ","")).split(",")
                i = 0
                while i < len(d):
                    tab[datas[d[i]]] = input(f"New {datas[d[i]]}: ")
                    i += 1
                    
                for elt in tab:
                    tab2.append(f"{elt} = '{tab[elt]}'")
            
            cursor.execute(f"""UPDATE contact SET {", ".join(tab2)} WHERE phone_number = {getContact}""")
            mydb.commit()
            print("The contact updated successfully!!!")
    # Delete the contact
    elif entry == 3:
        os.system('cls')
        print("My current contacts:")
        cursor.execute("""SELECT firstname, lastname, phone_number, email FROM contact;""")
        rows = cursor.fetchall()
        for row in rows:
            print("{0} {1} - {2} - {3}\n".format(row[0], row[1], row[2], row[3]))
        
        getContact = input("Which contact you'd like to delete? (Type only the phone number): ")
        cursor.execute("""SELECT * FROM contact WHERE phone_number = {}""".format(getContact))
        rows = cursor.fetchall()
        if len(rows) == 0:
            print("Contact not found!!!")
        else:
            cursor.execute("""DELETE FROM contact WHERE phone_number = {}""".format(getContact))
            mydb.commit()
            print("The contact has been deleted successfully!!!")
    # Display all the contacts
    elif entry == 4:
        os.system('cls')
        print("My current contacts:")
        cursor.execute("""SELECT firstname, lastname, phone_number, email FROM contact;""")
        rows = cursor.fetchall()
        for row in rows:
            print("{0} {1} - {2} - {3}\n".format(row[0], row[1], row[2], row[3]))
            