#3 Пользователь вводит длины трех сторон треугольника (a,b,c) [тип float]. Напишите программу, которая проверяет,
#является ли треугольник прямоугольным (с**2=a**2+b**2) 3, 4, 5

a = float(input('1 side : '))
b = float(input('2 side : '))
c = float(input('3 side : '))

if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print("Correct")
else:
    print("Not correct")

