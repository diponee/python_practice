# Simple Dictionary Phonebook in Python

phonebook = {}  # Initialize an empty dictionary

def add_contact(name, number):
    phonebook[name] = number
    print(f"{name} has been added with phone number {number}.")

def view_contacts():
    if not phonebook:
        print("Phonebook is empty.")
    else:
        print("Phonebook Contacts:")
        for name, number in phonebook.items():
            print(f"{name}: {number}")

def search_contact(name):
    if name in phonebook:
        print(f"{name}'s number is {phonebook[name]}")
    else:
        print(f"{name} not found in phonebook.")

def delete_contact(name):
    if name in phonebook:
        del phonebook[name]
        print(f"{name} has been deleted.")
    else:
        print(f"{name} not found.")

# Simple menu for the phonebook
while True:
    print("Phonebook Menu")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        name = input("Enter contact name: ")
        number = input("Enter contact number: ")
        add_contact(name, number)

    elif choice == '2':
        view_contacts()

    elif choice == '3':
        name = input("Enter name to search: ")
        search_contact(name)

    elif choice == '4':
        name = input("Enter name to delete: ")
        delete_contact(name)

    elif choice == '5':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

