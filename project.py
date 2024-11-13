class Contact:
    def __init__(self, contact_id, name, phone, email, address):
        self.contact_id = contact_id
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
    
    def __str__(self):
        return (f"ID: {self.contact_id}, Name: {self.name}, Phone: {self.phone}, "
                f"Email: {self.email}, Address: {self.address}")
    

class ContactManager:
    def __init__(self):
        self.contacts = {}
        self.next_contact_id = 1  # Start contact IDs from 1

    def add_contact(self, name, phone, email, address):
        contact_id = self.next_contact_id
        new_contact = Contact(contact_id, name, phone, email, address)
        self.contacts[contact_id] = new_contact
        self.next_contact_id += 1
        print(f"Contact '{name}' added successfully!")

    def view_contact(self, contact_id):
        if contact_id in self.contacts:
            print(self.contacts[contact_id])
        else:
            print("Contact not found!")

    def update_contact(self, contact_id, name=None, phone=None, email=None, address=None):
        if contact_id in self.contacts:
            contact = self.contacts[contact_id]
            if name:
                contact.name = name
            if phone:
                contact.phone = phone
            if email:
                contact.email = email
            if address:
                contact.address = address
            print(f"Contact ID {contact_id} updated successfully!")
        else:
            print("Contact not found!")

    def delete_contact(self, contact_id):
        if contact_id in self.contacts:
            del self.contacts[contact_id]
            print(f"Contact ID {contact_id} deleted successfully!")
        else:
            print("Contact not found!")

    def list_all_contacts(self):
        if self.contacts:
            for contact in self.contacts.values():
                print(contact)
        else:
            print("No contacts found.")
    
    def search_contacts(self, search_term):
        found = False
        for contact in self.contacts.values():
            if search_term.lower() in contact.name.lower() or search_term.lower() in contact.phone:
                print(contact)
                found = True
        if not found:
            print(f"No contacts found for '{search_term}'.")


def main():
    contact_manager = ContactManager()

    # Add some contacts
    contact_manager.add_contact("John Doe", "555-1234", "john.doe@example.com", "123 Elm Street")
    contact_manager.add_contact("Jane Smith", "555-5678", "jane.smith@example.com", "456 Oak Avenue")
    contact_manager.add_contact("Alice Johnson", "555-9876", "alice.johnson@example.com", "789 Pine Road")
    
    # List all contacts
    print("\nList of all contacts:")
    contact_manager.list_all_contacts()

    # View a specific contact
    print("\nView contact with ID 2:")
    contact_manager.view_contact(2)

    # Update contact information
    print("\nUpdating contact with ID 2:")
    contact_manager.update_contact(2, phone="555-4321", address="555 Maple Drive")
    contact_manager.view_contact(2)

    # Delete a contact
    print("\nDeleting contact with ID 1:")
    contact_manager.delete_contact(1)

    # List all contacts after deletion
    print("\nList of all contacts after deletion:")
    contact_manager.list_all_contacts()

    # Search for contacts
    print("\nSearching for contacts with the term 'Alice':")
    contact_manager.search_contacts("Alice")

if __name__ == "__main__":
    main()
