import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

from py.parse_inst import soup

vacancies_info = soup.find_all('p', class_='overflow')
for name in vacancies_info:
    print('https://www.work.ua'+name.a['href'])
for info in vacancies_info:
    print(info.text)


