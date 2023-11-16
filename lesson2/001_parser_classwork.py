# import requests
import re
# from requests.exceptions import HTTPError
#
# url = 'https://xkcd.com/353/'
#
# response = requests.get(url, timeout=10)
#
# # 200 - success
# # 300 - redirect
# # 400 - client error
# # 500 - server error
#
# # print(response.text)
#
# for url in ['https://api.github.com', 'https://api.github.com/invalid']:
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#     except HTTPError as http_err:
#         print(f'HTTP error occurred: {http_err}')
#     else:
#         print('Success')

# from bs4 import BeautifulSoup as BS
#
# url = 'https://www.gammatest.net/course/python'
#
# response = requests.get(url)
#
# soup = BS(response.content, 'html.parser')

# print(soup.div['class'])
# print(soup.a['href'])
#
# match = soup.find('div', class_='col-md-8')
# print(match.h2.text)

# matches = soup.find_all('script',type='text/javascript')
# print(soup.div.get_attribute_list('class'))

# matches = soup.tr.findChildren()
# print(matches)

import requests
from bs4 import BeautifulSoup as BS

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
usd_to_yen = 'https://www.google.com/search?q=usd+to+yen&oq=usd+to+yen&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDIyNDZqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8'\


response = requests.get(usd_to_yen, headers=headers)
soup = BS(response.content, 'html.parser')

data = soup.find('span', class_='DFlfde SwHCTb')
print(float(data.text.replace(',', '.')))
print(type(data['data-value']))