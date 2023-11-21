import pandas as pd

df = pd.read_csv('survey_results_public.csv')

while True:
    print("\nВыберите опцию:")
    print("1. Количество программистов по статусу хобби/профессионал")
    print("2. Статистика возраста программистов")
    print("3. Количество программистов по странам (в порядке убывания)")
    print("4. Таблица с валютами (в порядке возрастания)")
    print("0. Выйти")

    choice = input("Введите номер опции (0-4): ")

    if choice == '0':
        print("Выход из программы.")
        break
    elif choice == '1':
        hobbyist_count = df['Hobbyist'].value_counts()
        print("Количество программистов по статусу хобби/профессионал:")
        print(hobbyist_count)
    elif choice == '2':
        age_stats = df['Age'].agg(['mean', 'max', 'min'])
        print("\nСтатистика возраста программистов:")
        print(age_stats)
    elif choice == '3':
        country_counts = df['Country'].value_counts().sort_values(ascending=False)
        print("\nКоличество программистов по странам (в порядке убывания):")
        print(country_counts)
    elif choice == '4':
        unique_currencies = df['CurrencyDesc'].value_counts(ascending=True)
        print("\nТаблица с валютами (в порядке возрастания):")
        print(unique_currencies)
    else:
        print("Некорректный ввод. Пожалуйста, введите число от 0 до 4.")
