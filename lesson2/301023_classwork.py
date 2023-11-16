#
# def squares_generator(start, end):
#     for num in range(start, end + 1):
#         yield num ** 2
#
# def infinite_counter(start):
#     while True:
#         start += 1
#         yield start - 1
#
# x = squares_generator(1, 100)
#
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
import itertools

#
# #numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# #def squares(number):
# #    return number ** 2
#
# #new_nums = map(squares,numbers )
#
# #new_nums = []
# #for num in numbers:
# #    new_nums.append(squares(num))
# #
# #print(new_nums)
#
# #x = {
# #    '2134dasad131' : {
# #       'make': 'VW',
# #        'model': 'Golf',
# #    }
# #}
#
#
# def change_dict(d):
#     make, model, serial = d['make'], d['model'], d['serial']
#     return {
#         serial: {
#             'make': make,
#             'model': model
#         }
#     }
#
# cars = [
#     {
#         'make': 'VW',
#         'model': 'Golf',
#         'serial': '2134dasad131'
#     },
#     {
#         'make': 'BMW',
#         'model': '320i',
#         'serial': '2as1234dsvbd131'
#     },
#     {
#         'make': 'Seat',
#         'model': 'Leon',
#         'serial': 'sa23kmm322133'
#     }
# ]
#
# new_cars = map(change_dict, cars)
# print(list(new_cars))
#
# # def add_or_even(number):
# #     if number % 2 == 0:
# #         return True
# #     else:
# #         return False
# #
# # new = filter(add_or_even, nums1)
# # print(list(new))

# data1 = [1, 2, 3, 4, 5]
# data2 = ['mon', 'tue', 'wed', 'thu', 'fri']
#
# new = zip(data1, data2, data2, data1, range(10))
# print(list(new))

import itertools

# #
# # counter = itertools.count()
# #
# # print(list(zip([10, 20, 30, 40], counter)))
# #
# #data = [100, 200, 300, 400, 500]
# data2 = [5, 6, 7, 8, 9, 10, 11, 12, 13]
# #
# # print(list(itertools.zip_longest(data, data2)))
#
# counter = itertools.repeat(3)
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

letters = ['a', 'b', 'c', 'd']
numbers = [1, 2, 3, 4]
numbers2 = [4, 5, 4, 3, 2, 1, 0, 4, 9, 2, 0, 45]
selectors = [True, False, False, True]
names = ['Jack', 'Mary']

# result = itertools.combinations(range(10), 4)
# result = itertools.permutations(letters, 2)
# result = itertools.combinations_with_replacement(letters, 4)
# for c in result:
#     print(c)

# result = itertools.compress(letters, numbers)
# print(list(result))
#
# result = itertools.filterfalse(lambda x: x > 2, numbers2)
# print(list(result))

# result = itertools.dropwhile(lambda x: x > 2, numbers2)
# result = itertools.takewhile(lambda x: x > 2, numbers2)
# print(list(result))

# result = itertools.accumulate(numbers2)
# print(list(result))


people = [
    {
        'name': 'John Smith',
        'city': 'Berlin'
    },
    {
        'name': 'Mary Gold',
        'city': 'Berlin'
    },
    {
        'name': 'Taavi Tamm',
        'city': 'Berlin'
    },
    {
        'name': 'Piere Cardin',
        'city': 'Tallinn'
    },
    {
        'name': 'Jack Rock',
        'city': 'Tallinn'
    },
    {
        'name': 'Lee Hong',
        'city': 'Tallinn'
    },
    {
        'name': 'Abdul Faruh',
        'city': 'Dubai'
    },
    {
        'name': 'Mary Pierce',
        'city': 'Dubai'
    },
{
        'name': 'Lee Hong',
        'city': 'Tallinn'
    }
]

people.sort(key=lambda x: x['city'])
result = itertools.groupby(people, lambda x: x['city'])

for key, group in result:
    print(list(group))