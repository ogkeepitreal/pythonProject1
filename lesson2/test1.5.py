#5 Как известно, кортеж является неизменяемым типом. Напишите программу, которая позволяет в кортеж A добавить
# кортеж B таким образом, что кортеж B помещается на index[2].
#Пример: (1, 2, 3, 5, 8) (8,2,5) → (1, 2, 8, 2, 5, 3, 5, 8)

tuple_1 = (1, 2, 3, 5, 8)
tuple_2 = (8, 2, 5)

tuple_3 = tuple_1[0:2] + tuple_2 + tuple_1[2:5]

print(tuple_3)