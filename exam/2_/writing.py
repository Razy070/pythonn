# list1 = ["1", "2", "3"]  # чтобы распокавать нужно поставить *
# tuple1 = ["1", "2", "3"]  # чтобы распокавать нужно поставить *
# # print(list1)
# # print(tuple1)
# print(*list1)
# print(*tuple1)
#  # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# one = {
#     "name": "Roma",
#     "age": 15
# }
#
# print(one.values())
#
# print(list1 * 2)
#
# print([*list1, *tuple1])
#
# if "15" in list1:
#     print("yes")
# else:
#     print("no")
#
# if one.get("name", False) is False:
#     print("not have")
# else:
#     print("have")
#
#
# # print(one["name1"])
#
# def equal(dictionary: dict, key: str, new_value: any) -> bool:
#     if dictionary.get(key, False) is False:
#         dictionary[key] = any
#         return True
#     return False
#
#
# print(equal(one, "name1", "Roma"))
# print(equal(one, "name", "Roma"))
#
#
# class Techic:
#     def check_speed(self):
#        return "yes"
#
#  def __stop(self):
#         return True
#
# class Car(Techic):
#     def check_fuel(self):
#         return "have"
#
#     def check_speed(self):
#         return super().check_speed() * 2
#
#
# car = Car()
# print(car.check_speed())  # наследование
#
# print(car.check_fuel())  # полиморфизм
#
# # print(car._start()) # protected инкапуляция (сокрытие
#
# # print(car.__stop()) # приватный
#
# def name():
#     pass
#
#
# for i in range(1, 10):
#     pass
#
#
# print(range(1, 10), type(range(1, 10)))
#
# list2 = [i for i in range(1,10)]
# print(list2)
#
#
# str2 = "\t name".strip()
# print(str2)
#
# print("\t name")
# print("\t name ".strip())
#
# auth = True
#
# def decor(func):
#     print("1")
#     def start(*args,**kwargs):
#
#         return func(args,kwargs)
#
#     print("2")
#     return start
#
# @decor
# def one(dictionary):
#     print(dictionary)
#
#
# one(dictionary=dictionary)
