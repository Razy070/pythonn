import math
import requests
from bs4 import BeautifulSoup
import json
import time


# list1 = [10, 200]
# list2 = [True, 'Slova']
# list3 = list1 + list2
#
# print(*list3)
#
# turple1 = (True, "QW")
# turple2 = (*turple1, *list2)
#
# print(turple2)
#
# round(1.5)
# print(round(1.5))
#
# print(math.floor(4.4))
#
# print(float(1))
#
# print(int(4.4))
#
# str1 = "ABCD"
# for i in str1:
#     if i.lower() != "b":
#         print(i)
#
# list6 = [x for x in "ABCD" if x.lower() != "b"]
# print(list6)
#
# if 10 > 5 or 10 < 5:
#     print("Правда")
#
# str4 = "пайтон лучший язык"
# print(str4.split())
#
# for i in range(3, 6 + 1):
#     print(i)
#
# for i in range(0, -10, -2):
#     print(i)
#
# print(type(True))
#
#
# def sumator(var1: int, var2: float) -> float:
#     return var1 + var2
#
#
# res = sumator(10, 20.0)
# print(res)
#
#
# class Car:
#     oul = "растительное"
#     _oul2 = "минеральное"
#     __oul3 = "синтетика"
#
#
# car1 = Car
# print(car1.oul)
# print(car1._oul2)
# # print(car1.__oul3)
#
#
# dict_sample = {
#     "Company": "Toyota",
#     "model": "Premio",
#     "year": 2012
# }
#
# print(dict_sample["year"])
#######################################################################################
# url = 'https://jsonplaceholder.typicode.com/photos'
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                          'Chrome/102.0.0.0 Safari/537.36'}
# response = requests.get(url=url, headers=headers)
# soup = BeautifulSoup(response.text)
# print(soup)
# data = soup.find_all('article')
# print(data)
# print(len(data))
# response = requests.get("https://jsonplaceholder.typicode.com/photos")
# todos = json.loads(response.text)
#
# print(todos == response.json())  # True
# print(type(todos))  # <class 'list'>
#
# print(todos[:10])
################################################################
# hours = 0
# minutes = 0
# seconds = 0
#
# # код до цикла
# while True:
#     # seconds = seconds + 1
#     seconds += 1
#
#     if seconds > 59:
#         minutes += 1
#         seconds = 0
#
#     if minutes > 59:
#         hours += 1
#         minutes = 0
#
#     if hours > 23:
#         seconds = 0
#         minutes = 0
#         hours = 0
#
#     time.sleep(0.00001)
#     print(f"{hours}:{minutes}" + ":" + str(seconds))
# код после цикла

class Animal:
    def __init__(self, life):
        self.life = life / 2


class Tiger:
    def __init__(self, life):
        self.life = life * 9


animal1 = Animal(life=50)
tiger1 = Tiger(life=9)
print(tiger1.life)

