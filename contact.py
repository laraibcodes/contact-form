contacts=[]

def add_contacts():
    name = input("Enter contact name: ")
    phone = input("Enter phone/email: ")
    favourite = input("Mark as favourite? (yes/no): ").lower() == "yes"
    contacts.append({"name": name, "phone": phone, "favourite": favourite})
    print(f"{name} added to contacts!")
    input("Press Enter to continue...")  

def show_contacts():
    print("Contact list:")
    if not contacts:
        print("contact list is empty.")
    else:
        for contact in contacts:
            
            fav = "Favourite" if contact['favourite'] else "Not favourite"
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Favourite: {fav}")
    input("Press Enter to continue...") 

def favourite_contacts():
    print("Displaying favourite contacts")
    if not contacts:
        print("No favourite contacts marked yet.")
    else:
        found_fav = False 
        for contact in contacts:
            if contact['favourite']:
                fav = "Favourite"
                print(f"Name: {contact['name']}, Phone: {contact['phone']}, Favourite: {fav}")
                found_fav = True
        if not found_fav:
            print("No favourite contacts marked yet.")
    input("Press Enter to continue...") 
def search_contacts():
    search_name=input("Enter name to search in contacts: ")
    found=False
    for contact in contacts:
        
        if contact['name'].lower() == search_name.lower():
            print(f"Contact found: Name: {contact['name']}, Phone: {contact['phone']}")
            found=True
            break
    if not found:
        print("Contact not found.")
    input("Press Enter to continue...") 

def delete_contacts():
    delete_contact=input("Enter name to delete from contacts: ")
    found = False
    for contact in contacts:
       
        if contact['name'].lower() == delete_contact.lower():
            confirm = input(f"Are you sure you want to delete {contact['name']}? (yes/cancel): ").lower()
            if confirm == "yes":
                contacts.remove(contact)
                print(f"Contact {delete_contact} deleted.")
            else:
                print("Deletion cancelled.")
            found = True
            break
    if not found:
        print("Contact not found.")
    input("Press Enter to continue...")  
def exit_program():
    print("Exiting the contact form")
   
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
