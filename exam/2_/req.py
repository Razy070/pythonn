import requests
from bs4 import BeautifulSoup

url = 'http://universities.hipolabs.com/search?country=United+States'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/102.0.0.0 Safari/537.36'}
response = requests.get(url=url, headers=headers)
soup = BeautifulSoup(response.text)
print(soup)
data = soup.find_all('article')
print(data)
print(len(data))
