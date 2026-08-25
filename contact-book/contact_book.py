import json

filename = "contacts.json"


def load_contacts():
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_contacts(contacts):
    with open(filename, "w") as file:
        json.dump(contacts, file, indent=4)


def view_contacts(contacts):
    if not contacts:
        print("\nno contacts found! 📭")
        return

    print("\n===== CONTACTS =====")

    for name, details in contacts.items():
        print(f"\nname: {name}")
        print(f"phone: {details['phone']}")
        print(f"email: {details['email']}")


def add_contact(contacts):
    name = input("\nenter name: ").strip()

    if not name:
        print("name cannot be empty!")
        return

    if name in contacts:
        print("contact already exists!")
        return

    phone = input("enter phone number: ").strip()
    email = input("enter email: ").strip()

    contacts[name] = {
        "phone": phone,
        "email": email
    }

    save_contacts(contacts)
    print("contact added! ")


def search_contact(contacts):
    name = input("\nenter the name to search: ").strip()

    if name in contacts:
        details = contacts[name]

        print("\n===== CONTACT FOUND =====")
        print(f"name: {name}")
        print(f"phone: {details['phone']}")
        print(f"email: {details['email']}")
    else:
        print("contact not found! ")


def edit_contact(contacts):
    name = input("\nenter the name of the contact to edit: ").strip()

    if name not in contacts:
        print("contact not found!")
        return

    print("\nleave a field empty to keep the existing information.")

    phone = input(f"phone [{contacts[name]['phone']}]: ").strip()
    email = input(f"email [{contacts[name]['email']}]: ").strip()

    if phone:
        contacts[name]["phone"] = phone

    if email:
        contacts[name]["email"] = email

    save_contacts(contacts)
    print("contact updated! ️")


def delete_contact(contacts):
    name = input("\nenter the name of the contact to delete: ").strip()

    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("contact deleted! ️")
    else:
        print("contact not found!")


contacts = load_contacts()

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. view contacts")
    print("2. add contact")
    print("3. search contact")
    print("4. edit contact")
    print("5. delete contact")
    print("6. exit")

    choice = input("\nchoose an option: ").strip()

    if choice == "1":
        view_contacts(contacts)

    elif choice == "2":
        add_contact(contacts)

    elif choice == "3":
        search_contact(contacts)

    elif choice == "4":
        edit_contact(contacts)

    elif choice == "5":
        delete_contact(contacts)

    elif choice == "6":
        print("goodbye! ")
        break

    else:
        print("invalid choice. please try again.")
