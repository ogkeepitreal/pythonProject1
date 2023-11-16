# Пользователь вводит имя и фамилию, в консоль выводится имя и фамилия с больщой буквы
user_name = input('Your name : ')
user_surename = input('Your surname : ')
print('Your full name is : ' + user_name.capitalize() + ' ' + user_surename.capitalize())



# Удалите все знаки препинания из строки
import string
sample = 'Hello, my name is Jack! I am from London - United Kingdom. Where are you from?'

delete_symbols = str.maketrans('', '', string.punctuation)
without_symbols = sample.translate(delete_symbols)

print(without_symbols)



# Пользователь вводит произвольную строку, выведете её длину не учитывая пробелы
text = input('Text : ')
spacebutton = ' '
spacebutton_count = text.count(spacebutton)
text_count = len(text)
list_result = text_count - spacebutton_count
print(list_result)



# Выведите в консоль строку с адресом '..\new_dir\tables.py'.
print('\'..\\new_dir\\tables.py\'')
