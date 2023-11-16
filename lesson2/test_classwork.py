#Написать программу, запрашивающую имя, фамилию и возраст пользователя и выводящую строку вида:
#Hello, <Фамилия пользователя> <Имя пользователя>. Your age is: <возраст>

name = input('Your name : ')
surename = input('Your surename : ')
age = input('Your age : ')

print(f'Hello, {surename} {name}. Your age is: {age}')


#2 Напишите программу, которая находит длину гипотенузы для прямоугольного треугольника по двум катетам. (
#с = sqrt(a * a  +  b * b))

a = float(input('Первый катет : '))
b = float(input('Второй катет : '))
c = (a**2 + b**2)**0.5

print(c)


#3 Пользователь вводит длины трех сторон треугольника (a,b,c) [тип float]. Напишите программу, которая проверяет,
#является ли треугольник прямоугольным (с**2=a**2+b**2) 3, 4, 5

a = float(input('1 side : '))
b = float(input('2 side : '))
c = float(input('3 side : '))

if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print("Correct")
else:
    print("Not correct")


#4 Пользователь вводит некоторый произвольный список list. Написать программу, выводящую элементы списка в обратном порядке.

input_str = input("List : ")
input_list = input_str.split()

reversed_list = input_list[::-1]

print("Reversed list : ", reversed_list)


#5 Как известно, кортеж является неизменяемым типом. Напишите программу, которая позволяет в кортеж A добавить
# кортеж B таким образом, что кортеж B помещается на index[2].
#Пример: (1, 2, 3, 5, 8) (8,2,5) → (1, 2, 8, 2, 5, 3, 5, 8)

tuple_1 = (1, 2, 3, 5, 8)
tuple_2 = (8, 2, 5)

tuple_3 = tuple_1[0:2] + tuple_2 + tuple_1[2:5]

print(tuple_3)



#7 *Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.
#    Примеры:
#    1234565 seconds = 14:6:56:5
user_input = int(input('Seconds: '))

seconds = user_input

days = seconds // 86400
seconds %= 86400

hours = seconds // 3600
seconds %= 3600

minutes = seconds // 60
seconds %= 60

remaining_seconds = seconds


formatted_time = f"{days}:{hours}:{minutes}:{remaining_seconds}"

print(f"{user_input} seconds = {formatted_time}")