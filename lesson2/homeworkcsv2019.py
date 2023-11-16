import csv

with open('2019.csv', 'r') as file:






top = 10
colum = 5

def sort_by_column

def change_top():
    global top





while True:
    user_choice = input('1.GDP per capita\n'
                        '2.Social support\n'
                        '3.Healthy life expectancy\n'
                        '4.Freedom to make life choices\n'
                        '5.Generosity\n'
                        '6.Perceptions of corruption\n'
                        '7.Change Top amount\n'
                        '0.Exit\n'
                        '--> ')
    if user_choice == '1':
        print(sort_by_column(3, top))
    elif user_choice == '2':
        print(sort_by_column(4, top))
    elif user_choice == '3':
        print(sort_by_column(5, top))
    elif user_choice == '4':
        print(sort_by_column(6, top))
    elif user_choice == '5':
        print(sort_by_column(7, top))

