# -*- coding: utf-8 -*-
"""
# Об’єкти
Python володіє потужними об'єктно-орієнтованими можливостями. Наприклад, усі змінні, функції і класи є об’єктам і володіють атрибутами і методами.
"""
a=1 # створити змінну (об'єкт класу int) і присвоїти їй 1
print a.__class__ # атрибут __class__ (клас об'єкта)
print a.__class__.__name__ # тип також є об'єктом і має атрибут __name__ (ім'я)
b=a.__add__(2) # метод __add__ повертає суму a+2
b=a+2 # або так
x=a.__float__() # метод повертає дійсне число x=float(a)
print a.__str__() # метод повертає рядок str(a)
