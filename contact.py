import sqlite3

def init_db():
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        phone TEXT,
        favourite INTEGER
    )
    """)

    conn.commit()
    conn.close()
def add_contacts():
   
    name = input("Enter contact name: ")
    phone = input("Enter phone/email: ")
    favourite = input("Mark as favourite? (yes/no): ").lower() == "yes"

   

    
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO contacts (name, phone, favourite) VALUES (?, ?, ?)",
        (name, phone, int(favourite))  
    )
    conn.commit()
    conn.close()

    print(f"{name} added to contacts successfully!")
    input("Press Enter to continue...")
 

def show_contacts():
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, phone, favourite FROM contacts")
    rows = cursor.fetchall()
    
    print("Contact list:")
    if not rows:
        print("Contact list is empty.")
    else:
        for row in rows:
            name, phone, favourite = row
            fav = "Favourite" if favourite else "Not favourite"
            print(f"Name: {name}, Phone: {phone}, Favourite: {fav}")
    conn.close()
    input("Press Enter to continue...")
def favourite_contacts():
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, phone FROM contacts WHERE favourite = 1")
    rows = cursor.fetchall()
    print("Favourite Contacts:")
    if not rows:
        print("No favourite contacts marked yet.")
    else:
        for row in rows:
            name, phone = row
            print(f"Name: {name}, Phone: {phone}, Favourite: Favourite")
    conn.close()
    input("Press Enter to continue...")
def search_contacts():
    search_name = input("Enter name to search in contacts: ")
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, phone, favourite FROM contacts WHERE LOWER(name) = ?", (search_name.lower(),))
    row = cursor.fetchone()
    if row:
        name, phone, favourite = row
        fav = "Favourite" if favourite else "Not favourite"
        print(f"Contact found: Name: {name}, Phone: {phone}, Favourite: {fav}")
    else:
        print("Contact not found.")
    conn.close()
    input("Press Enter to continue...")
def delete_contacts():
    delete_name = input("Enter name to delete from contacts: ")
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM contacts WHERE LOWER(name) = ?", (delete_name.lower(),))
    result = cursor.fetchone()
    
    if result:
        contact_id, name = result
        confirm = input(f"Are you sure you want to delete {name}? (yes/cancel): ").lower()
        if confirm == "yes":
            cursor.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
            conn.commit()
            print(f"Contact {name} deleted.")
        else:
            print("Deletion cancelled.")
    else:
        print("Contact not found.")
    
    conn.close()
    input("Press Enter to continue...")    
def exit_program():
    print("Exiting the contact form")
init_db()
print("Welcome to the Contact Form")

while True:
    print("1. Add contacts")
    print("2. Show Contacts")
    print("3. Favourite Contacts")
    print("4. Search Contacts")
    print("5. Delete Contacts")
    print("6. Exit")
    try:
        choice=int(input("Enter your choice:"))
    except ValueError:
        print("Invalid input. Please enter a number 1-6.")
        continue  
    if choice==1:
        add_contacts()
    elif choice==2:
        show_contacts()
    elif choice==3:
        favourite_contacts()
    elif choice==4:
        search_contacts()
    elif choice==5:
        delete_contacts()
    elif choice==6:
        exit_program()
        break
    else:
        print("Invalid choice, please try again.")
