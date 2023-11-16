#Написать программу, которая для произвольного списка находит число /
#числа, наиболее часто встречающееся в данном списке и возвращающее их также в виде списка.
#    Примеры:
#    [1, 2, 3, 4, 7, 9, 9] → [9]
#    [1, 2, 4, 6, 4, 6] → [4,6]


from collections import Counter


def find_most_frequent_numbers(input_list):
    # Используем Counter для подсчета количества каждого элемента в списке
    counts = Counter(input_list)

    # Находим максимальное количество повторений
    max_count = max(counts.values())

    # Формируем список чисел, которые встречаются максимальное количество раз
    most_frequent_numbers = [number for number, count in counts.items() if count == max_count]

    return most_frequent_numbers