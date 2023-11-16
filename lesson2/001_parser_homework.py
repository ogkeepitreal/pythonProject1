import requests
from bs4 import BeautifulSoup

# Выполните HTTP-запрос для получения HTML-кода веб-страницы
url = 'https://www.ilmateenistus.ee/ilm/ilmavaatlused/vaatlusandmed/oopaevaandmed/'
response = requests.get(url)
html = response.text

# Создайте объект BeautifulSoup для разбора HTML-кода
soup = BeautifulSoup(html, 'html.parser')

# Извлеките данные, например, температуры
temperature_data = []

# Найдите элементы, содержащие температуры
temperature_elements = soup.find_all('td', class_='last')  # Это пример селектора, который подходит для данных на этой странице

for element in temperature_elements:
    temperature_data.append(element.get_text())

# Выведите извлеченные данные
for temperature in temperature_data:
    print(temperature)
