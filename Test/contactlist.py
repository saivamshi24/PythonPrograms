class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"

class ContactList:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.contacts.append(contact)
        print(f"Contact {name} added successfully.")

    def display_contacts(self):
        if not self.contacts:
            print("No contacts in the list.")
        else:
            for contact in self.contacts:
                print(contact)

    def search_contact(self, search_term):
        found_contacts = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone or search_term in contact.email]
        if not found_contacts:
            print("No matching contacts found.")
        else:
            for contact in found_contacts:
                print(contact)

    def update_contact(self, search_term, new_name=None, new_phone=None, new_email=None):
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone or search_term in contact.email:
                if new_name:
                    contact.name = new_name
                if new_phone:
                    contact.phone = new_phone
                if new_email:
                    contact.email = new_email
                print(f"Contact updated: {contact}")
                return
        print("No matching contact found to update.")

    def delete_contact(self, search_term):
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone or search_term in contact.email:
                self.contacts.remove(contact)
                print(f"Contact {contact.name} deleted successfully.")
                return
        print("No matching contact found to delete.")

def main():
    contact_list = ContactList()
    while True:
        print("\nContact List Menu:")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            contact_list.add_contact(name, phone, email)
        elif choice == '2':
            contact_list.display_contacts()
        elif choice == '3':
            search_term = input("Enter name, phone, or email to search: ")
            contact_list.search_contact(search_term)
        elif choice == '4':
            search_term = input("Enter name, phone, or email to search for the contact to update: ")
            new_name = input("Enter new name (or leave blank to keep current): ")
            new_phone = input("Enter new phone number (or leave blank to keep current): ")
            new_email = input("Enter new email (or leave blank to keep current): ")
            contact_list.update_contact(search_term, new_name or None, new_phone or None, new_email or None)
        elif choice == '5':
            search_term = input("Enter name, phone, or email to search for the contact to delete: ")
            contact_list.delete_contact(search_term)
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
