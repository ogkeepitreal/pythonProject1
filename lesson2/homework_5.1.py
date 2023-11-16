# 1
# Напишите программу которая сложит все числа в заданном списке
# выведет результат в консоль
nums1 = [5, 6, 92, 47, 12, -18, 33, 8]

result = sum(nums1)
print(result)

# 2
# Напишите программу которая добавит в список edited_names словари
# с двумя парами { "name": "имя с большой буквы", "nameLength": "длина имени"}
names = ['jack', 'sarah', 'mary', 'joey', 'chris', 'samantha'];
edited_names = [];

for name in names:
    edited_name = name.capitalize()
    name_length = len(name)

    name_info = {'name': edited_name, 'nameLength': name_length}

    edited_names.append(name_info)

for item in edited_names:
    print(item)

# 3
# Напишите программу которая в список edited_nums добавит словари
# с тремя парами { "number": "само число", "square": "число в квадрпате", "cube": "число в кубе"}
nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9];
edited_nums = [];


for num in nums2:
    square = num ** 2
    cube = num ** 3
    num_info = {'number': num, 'square': square, 'cube': cube}
    edited_nums.append(num_info)
for item in edited_nums:
    print(item)

# 4
# напишите программу которая выводит в консоль сумму всех
# четных чисел в списке

nums_list = [1, 12, 34, 71, 14, 12, 33, 70, 82, 81, 9, 19, 90];

even_numbers = [num for num in nums_list if num % 2 == 0]
sum_of_even_numbers = sum(even_numbers)

print('Сумма четных чисел в списке:', sum_of_even_numbers)


# 5
# напишите программу которая проанализирует данный список и выведет в консоль самую длинную строку

some_strings = ['Star', 'Planet', 'Comet', 'Interstellar', 'Space'];

longest_string = max(some_strings, key=len)
print(longest_string)

# 6
# напишите программу которая возьмёт из данного списка наименования книг которые вышли в этом году
# и добавит их в новый список

books = [
    {
        'author': 'Jeremy Brook',
        'title': 'My childhood',
        'release': 2023
    },
    {
        'author': 'Samantha Jhones',
        'title': 'Living with ten cats',
        'release': 2020
    },
    {
        'author': 'Bob Summers',
        'title': 'Exploring far space',
        'release': 2021
    },
    {
        'author': 'Bill Brown',
        'title': 'Insects in our garden',
        'release': 2023
    },
    {
        'author': 'Jessica Love',
        'title': 'Programming for begginers',
        'release': 2023
    }
];

current_year = 2023
current_year_books = []

for book in books:
    if book['release'] == current_year:
        current_year_books.append(book['title'])

print('Current year books : ', current_year_books)

# 7
# Напишите функцию которая будет принимать два аргумента (start, end)
# Для каждого числа в диапозоне от start до end будет выводить число
# И Четное оно Или нечетное

def check_even_or_odd(start, end):
    for number in range(start, end + 1):
        if number % 2 == 0:
            print(f'{number} - четное число')
        else:
            print(f'{number} - нечетное число')


check_even_or_odd(1, 10)