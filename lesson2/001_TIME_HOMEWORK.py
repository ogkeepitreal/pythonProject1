from datetime import datetime

def string_to_datetime(input_string):
    try:
        if input_string[0:3].isalpha():
            date_obj = datetime.strptime(input_string, '%b %d %Y %I:%M%p')
        elif '/' in input_string:
            if input_string.count('/') == 2:
                # Добавляем нули для года, чтобы преобразование прошло успешно
                input_string = '00/' + input_string
                date_obj = datetime.strptime(input_string, '%y/%m/%d %H:%M')
            else:
                date_obj = datetime.strptime(input_string, '%d/%m/%y %H:%M')
        elif ',' in input_string:
            date_obj = datetime.strptime(input_string, '%A, %B %d, %Y')
        else:
            date_obj = datetime.strptime(input_string, '%d.%m.%Y - %H:%M:%S')

        return date_obj
    except ValueError:
        return None

# Запрос у пользователя ввода
user_input = input("Введите дату в одном из форматов (например, '14:20 10/12/22'): ")

# Преобразование введенной строки в объект datetime
date = string_to_datetime(user_input)

if date:
    print(f"Преобразованная дата: {date}")
else:
    print("Неверный формат даты.")

'''
sample1 = 'Jan 1 2014 2:43PM'
sample2 = '14:20 10/12/22'  # YY/MM/DD
sample3 = 'Tuesday, September 24, 2019'
sample4 = '01.01.1970 - 00:00:01'
'''