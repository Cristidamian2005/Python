# name = "Jon"
# school = "Radu Negru"
# print("{} works at {} .".format(name, school))
import random

import self as self


#functions

# def addition():
#     a = int(input(" Baga a: "))
#     b = int(input(" Baga b: "))
#     print(f"Suma = {a + b}")
#
#
# addition()

#kwargs

# def user_info(name, age=0, city="Tucson"):
#     '''This function prints name age city '''
#     print(f'{name} is {age} years old and from {city}')
# user_info("jon", 54, "Fagaras")
# user_info("Mihai")
# user_info("Relu", age = 35, city="Sibiu")
# user_info(name = "Ion", age = 35,)

# /////////  https://realpython.com/python-kwargs-and-args/#:~:text=Just%20as%20non%2Ddefault%20arguments,must%20come%20before%20**kwargs%20.
# *args and

# def add(*args):
#     print((sum(args)))
#
# print(f' suma este {add(1,2,3,4)}')

# sum_integers_args_2.py
# def my_sum(*integers):
#     result = 0
#     for x in integers:
#         result += x
#     return result
#
# print(my_sum(1, 2, 3))

## **kwargs
# def my_function(**kid):
#   print("His last name is " + kid["lname"])
#
# my_function(fname = "Tobias", lname = "Refsnes")


# sum_integers_args_3.py
# def my_sum(*args):
#     result = 0
#     for x in args:
#         result += x
#     return result
#
# list1 = [1, 2, 3]
# list2 = [4, 5]
# list3 = [6, 7, 8, 9]
#
# print(my_sum(*list1, *list2, *list3))

# # string_to_list.py
# a = [*"RealPython"]
# print(a)

# # mysterious_statement.py
# *a, = "RealPython"
# print(a)

#conditionals

# name = input("What is your name? ")
# if name == "Jessica":
#     print(f'Hello {name}')
#
# print('Have a nice day')

# def add():
#     a = float(input("Enter a number: "))
#     b = float(input("Enter another number: "))
#     print(a + b)
#
#
# def substraction():
#     a = float(input("Enter a number: "))
#     b = float(input("Enter another number: "))
#     print(a - b)
#
#
# def multiply():
#     a = float(input("Enter a number: "))
#     b = float(input("Enter another number: "))
#     print(a * b)
#
#
# def divide():
#     a = float(input("Enter a number: "))
#     b = float(input("Enter another number: "))
#     print(a / b)
#
# operation = input("Please type + - * or / : ")
# if operation == '+':
#     add()
# elif operation == '-':
#     substraction()
# elif operation =='*':
#      multiply()
# elif operation == '/':
#     divide()
# else:
#     print('Caracterul ales nu este operator')

# add()
# substraction()
# multiply()
# divide()

#loops
#for
# fruits = ['apples', 'oranges', 'pears', 'cherries', 'grapes']
# for fruit in fruits:
#     print('Would you like ' + fruit + '?')
# for number in range(1, 11):
#     print(f'Number {number}')

#while
# temp_f = 40
# while temp_f > 32:
#     print(f"the water is {temp_f}")
#     temp_f -= 1

# loop control

# temp_f = 40
# while temp_f > 32:
#     print(f"the water is {temp_f}")
#     temp_f -= 1
#     if temp_f == 33:
#         break

# for number in range(1, 11):
#     if number == 7:
#         print('we\' skipping number 7 ' )
#         continue
#     print(f"this is the number {number}")
#
# for number in range(1, 11):
#     if number == 3:
#         pass
#     else:
#          print(f"number is {number}")




# # #lists
# fruits = ['peaches', 'apples', 'pears', 'apples']
# years = [3, "1998", 2.5, 987, '1994']
#
# print("apple" in fruits)
# print("apples" in fruits)
# print(fruits.count("apples"))
# print(fruits.index("apples"))


# print(fruits, years)
#
# fruits.append('oranges')
# print(fruits)
#
# fruits.extend(years)
# print(fruits)
#
# fruits.remove("oranges")
# print(fruits)
#
# fruits.pop(0)
# print(fruits)
#
# fruits.pop(-1)
# print(fruits)
#
# # fruits.sort(fruits) - u poate face sortarea pentru ca itemii sunt de tip diferit
#
# numbers = [5, 67, 345, 234.66, 1, -654]
# numbers.sort()
# print(numbers)

#dictionaries

# stuff = {"food" : 15, "energy" : 100, 'enemies' : 3}
# print(stuff.get("food"))
# print(stuff.items())
# print(stuff.keys())

# stuff.pop("food")
# print(stuff)

# print(stuff.setdefault('food'))
# print(stuff)
# print(stuff.setdefault("friends", 123))
# print(stuff)
#
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
#
# x = car.setdefault("model", "Bronco")
#
# print(x)

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
#
# x = car.setdefault("color", "white")
#
# print(x)
# print(car)

# stuff = {"food" : 15, "energy" : 100, 'enemies' : 3}
# new_items = {'rocks' : 4, "arrows" : 18}
# stuff.update(new_items)
# print(stuff)
#
# new_items = {'rocks' : 2, "arrows" : 10}
# stuff.update(new_items)
# print(stuff)
#
# up_new = {"food" : 3, "webs" : 2}
# stuff.update(new_items)
# print(stuff)


#classes

# class Person:
#     def __init__(self, fn, ln, h, s):
#         "un fel de constructor in java"
#         self.fn = fn
#         self.ln = ln
#         self.h = h
#         self.s = s
#
#     def introduce(self):
#         print(f'Hello, my name is {self.fn} {self.ln}')
#
#     def emote(self):
#         emotion = random.randrange(1,3)
#         if emotion == 1:
#             print(f'{self.fn} is happy')
#         elif emotion == 2:
#             print(f'{self.fn} is sad ')
#
#     def status_change(self):
#         if self.h == 100:
#             print(f'{self.fn} is totally health')
#         elif self.h >= 76:
#             print(f'{self.fn} is a little tired')
#         elif self.h >= 51:
#             print(f'{self.fn} feels unwell')
#         elif self.h >= 25:
#             print(f'{self.fn} goes to doctor')
#         else:
#             print(f'{self.fn} is unconscious')
# Maria = Person("Maria", 'Mirea', 95, True)
# Rey = Person('Rey', 'Jones', 78, False)
#
# print(f'Is {Maria.fn} my friend? {Maria.s}')
#
# Maria.introduce()
# Rey.introduce()
#
# Maria.status_change()
# Rey.status_change()
#
# #inheritance, multiple inheritance, polymorphism
#
# class Enemy(Person):
#     #practic creeam un enemy connstructor (ca in Java)
#     def __init__(self, weapon, fn, ln, h, s):
#         super().__init__(fn, ln, h, s)
#         self.weapon = weapon
#
#     def hurt(self, other):
#         if self.weapon == 'rock':
#             other.h -= 10
#         elif self.weapon == 'stick':
#             other.h -= 5
#         print(other.h)
#
#     def insult(self, other):
#         if other.h <= 80:
#             print(f'{other.fn} you are tired and weak')
#
#     def steal(self, other):
#         print(f'{other.fn} ha ha ha , I have your stuff!')
#         if other.s == True:
#             other.s = False
#
# Alex = Enemy('rock', 'Alex', 'Wayne', 75, s = False)
# Alex.hurt(Maria)
# Alex.insult(Rey)
# Alex.steal(Maria)

# ### Multiple inheritance
#
# #Parent class 1
# class Item():
#     def __init__(self, sku):
#         self.sku = sku
#
#     def print_sku(self):
#         print(f'the sku is {self.sku}')
#
# #Parent class 2
# class Garment():
#     def __init__(self, section, type):
#         self.section = section
#         self.type = type
#
#     def print_Garment(self):
#         print(f'The Garment is in section {self.section} {self.type}')
#
#
# #Child Class
# class Shirts(Item, Garment):
#     def __init__(self, sku, section, type, name, color):
#         self.name = name
#         self.color = color
#         Item.__init__(self, sku)
#         Garment.__init__(self, section, type)
#
#     def print_shirt(self):
#         print(f'{self.color} {self.name} on sale!')
#
# Blouse = Shirts("00001", 43, 'Tops', 'Formal Blouse', 'White')
# Blouse.print_sku()
# Blouse.print_Garment()
# Blouse.print_shirt()

# Polymorphism (method override)




