#4 Пользователь вводит некоторый произвольный список list. Написать программу, выводящую элементы списка в обратном порядке.

input_str = input("List : ")
input_list = input_str.split()

reversed_list = input_list[::-1]

print("Reversed list : ", reversed_list)