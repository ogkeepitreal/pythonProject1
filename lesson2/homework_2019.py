import csv

data = []
with open("2019.csv", newline="") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        data.append(row)

print("Меню:")
print("1. GDP per capita")
print("2. Social support")
print("3. Healthy life expectancy")
print("4. Freedom to make life choices")
print("5. Generosity")
print("6. Perceptions of corruption")

try:
    select_column = int(input("Выберите номер столбца для сортировки (1-6): ")) - 1
    if select_column < 0 or select_column > 5:
        print("Неверный выбор столбца.")
        exit()
except ValueError:
    print("Введите число от 1 до 6.")
    exit()

try:
    num_countries = int(input("Введите количество стран для вывода: "))
except ValueError:
    print("Введите число.")

sorted_data = sorted(data, key=lambda x: float(x[select_column]), reverse=True)

print(f"Топ {num_countries} стран по столбцу {select_column + 1}:")

for i, row in enumerate(sorted_data[:num_countries], start=1):
    print(f"{i}. {row[1]} ({row[select_column]})")
