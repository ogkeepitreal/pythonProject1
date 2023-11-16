contact_book = {}

def add_contact(name, phone, email):
    if name not in contact_book:
        contact_book[name] == {
            'phone': phone,
            'email': email
        }
        print(f'Contact {name} was succsessfully added.')
    else:
        print(f'Contact {name} already exists!')


def view_contact(name):
    if name in contact_book:
        contacts = contact_book[name]
        print(f'Name: {name}, Phone: {contacts['phone']}, Email: {contacts['email']}')
    else:
        print(f'Contact {name} does not exist.')


def update_contact(name, phone, email):
    if name in contact_book:
        contact_book[name].update({'phone': phone, 'email': email})
        print(f'Contact {name} does not exist.')


def delete_contacts(name):
    if name in contact_book:
        del contact_book[name]
        print(f'Contact {name} was succsessfully deleted')
    else:
        print(f'Contact {name} does not exist.')