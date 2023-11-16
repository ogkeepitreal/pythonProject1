contacts = {}

def add_contact():
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    email = input("Введите адрес электронной почты: ")

    if name not in contacts:
        contacts[name] = {'phone': phone, 'email': email}
        print(f'Контакт: \n Имя: {name} \n Телефон: {phone} \n Почта: {email} \n успешно добавлен.')
    else:
        print(f'Контакт {name} уже существует.')
def view_contact(name):
    if name in contacts:
        contact = contacts[name]
        print(f'Имя: {name}')
        print(f'Телефон: {contact['phone']}')
        print(f'Email: {contact['email']}')
    else:
        print(f'Контакт {name} не найден.')

def update_contact(name):
    if name in contacts:
        phone = input('Введите новый номер телефона: ')
        email = input('Введите новый адрес электронной почты: ')
        contacts[name]['phone'] = phone
        contacts[name]['email'] = email
        print(f'Контакт {name} успешно обновлен.')
    else:
        print(f'Контакт {name} не найден.')

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f'Контакт {name} успешно удален.')
    else:
        print(f'Контакт {name} не найден.')

while True:
    print('Меню:\n1. Добавить контакт\n2. Просмотреть контакт\n3. Обновить контакт\n4. Удалить контакт\n5. Выход')

    choice = input('Выберите действие (1/2/3/4/5): ')

    if choice == '1':
        add_contact()
    elif choice == '2':
        name = input('Введите имя контакта: ')
        view_contact(name)
    elif choice == '3':
        name = input('Введите имя контакта: ')
        update_contact(name)
    elif choice == '4':
        name = input('Введите имя контакта: ')
        delete_contact(name)
    elif choice == '5':
        quit()
    else:
        print('Некорректный выбор. Попробуйте снова.')