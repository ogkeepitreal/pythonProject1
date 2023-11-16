import csv

# Функция для загрузки данных из CSV файла
def load_data(file_path):
    data = []
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Пропустить заголовок
        for row in reader:
            data.append(row)
    return data

# Функция для вывода топ 10 стран по выбранному столбцу
def top_10_countries(data, column_index):
    sorted_data = sorted(data, key=lambda x: float(x[column_index]), reverse=True)
    return sorted_data[:10]

# Основная часть программы
file_path = '2019.csv'
data = load_data(file_path)

# Выберите индекс столбца, по которому вы хотите составить рейтинг (например, Score - 2)
selected_column_index = 2

# Получите топ 10 стран по выбранному столбцу
top_countries = top_10_countries(data, selected_column_index)

# Выведите результат
print("Топ 10 стран:")
for i, row in enumerate(top_countries, start=1):
    print(f"{i}. {row[1]} ({row[selected_column_index]})")
