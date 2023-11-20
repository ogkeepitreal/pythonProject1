import mysql.connector


db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Sukapidarasq123',
    database='sakila'
)

mycursor = db.cursor()

search_name = input("Имя для поиска: ")
sql_query = "SELECT * FROM actor WHERE first_name =%s"

mycursor.execute(sql_query, (search_name,))

result = mycursor.fetchall()

if result:
    for row in result:
        print(row)
else:
    print("Указанные имена не найдены.")

