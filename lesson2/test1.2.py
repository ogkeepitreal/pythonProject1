test_list = [1, 2, 3, 4, 4, 5, 5, 5, 7, 8, 8, 8, 10, 10]

max_count = 0
result = []

for num in test_list:
    if test_list.count(num) > max_count:
        max_count = test_list.count(num)

for num in test_list:
    if test_list.count(num) == max_count and num not in result:
        result.append(num)

print(result)