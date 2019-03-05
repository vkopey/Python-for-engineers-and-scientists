# -*- coding: utf-8 -*-
"""
# copy - копії об'єктів
Модуль `copy` призначений для створення поверхневих і глибоких копій складених об'єктів. Функція `copy` створює поверхневу копію шляхом копіювання посилань на атрибути об'єкта. Функція `deepcopy` створює глибоку копію шляхом рекурсивного створення окремих копій атрибутів об'єкта.
"""
import copy
class A(object): pass # клас A
class B(object): pass # клас B    
a=A() # об'єкт a
b=B() # об'єкт b
a.x=b # атрибут x
b.y=5 # атрибут y
copy_a=copy.copy(a) # поверхнева копія об'єкта
print a, a.x, a.x.y
print copy_a, copy_a.x, copy_a.x.y
copy_a=copy.deepcopy(a) # повністю незалежна глибока копія об'єкта
print copy_a, copy_a.x, copy_a.x.y
