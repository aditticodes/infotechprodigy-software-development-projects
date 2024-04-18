import json

def load_contacts():
    try:
        with open('contacts.json', 'r') as f:
            return json.load(f)
    except:
        return []

def save_contacts(contacts):
    with open('contacts.json', 'w') as f:
        json.dump(contacts, f)

def add_contact(contacts, name, phone, email):
    contacts.append({'name': name, 'phone': phone, 'email': email})
    save_contacts(contacts)

def delete_contact(contacts, name):
    contacts = [contact for contact in contacts if contact['name'] != name]
    save_contacts(contacts)

def edit_contact(contacts, name, new_phone=None, new_email=None):
    for contact in contacts:
        if contact['name'] == name:
            if new_phone:
                contact['phone'] = new_phone
            if new_email:
                contact['email'] = new_email
            save_contacts(contacts)
            return
    print('Contact not found')

def view_contacts(contacts):
    for contact in contacts:
        print(contact['name'], contact['phone'], contact['email'])

contacts = load_contacts()

while True:
    print('\nContact Management System')
    print('1. Add contact')
    print('2. Delete contact')
    print('3. Edit contact')
    print('4. View contacts')
    print('5. Exit')

    choice = int(input('Enter your choice: '))

    if choice == 1:
        name = input('Enter name: ')
        phone = input('Enter phone: ')
        email = input('Enter email: ')
        add_contact(contacts, name, phone, email)
        print('contact is successfully saved')

    elif choice == 2:
        name = input('Enter name of contact to delete: ')
        delete_contact(contacts, name)
        print('contact is deleted successfully')

    elif choice == 3:
        name = input('Enter name of contact to edit: ')
        new_phone = input('Enter new phone (leave blank to keep unchanged): ')
        new_email = input('Enter new email (leave blank to keep unchanged): ')
        edit_contact(contacts, name, new_phone, new_email)

    elif choice == 4:
        view_contacts(contacts)

    elif choice == 5:
        break

    else:
        print('Invalid choice. Please try again.')1