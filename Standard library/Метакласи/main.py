# -*- coding: utf-8 -*-
"""
# Метакласи
Метакласи - це об'єкти, які створюють класи. Відомим метакласом є функція `type`. Метакласи використовуються для створення класів на етапі виконання. Нижче показані різні способи використання метакласів.
"""
def cls_factory(a,fn): # функція створює новий клас з атрибутами `a`,`fn`
    class C(object):pass # пустий клас, успадкований від object
    setattr(C,'a',a) # установити атрибут `a`
    setattr(C, fn.__name__, fn) # установити атрибут `fn`
    return C # повернути клас
def method1(self): # метод класу
  print self.a # вивести значення атрибута `a`
Class1 = cls_factory(1,method1) # створити клас Class1
obj1 = Class1() # створити об'єкт obj1
obj1.method1() # викликати метод method1

#створити клас за допомогою метакласу type
Class2 = type('Class2', (object,), {'a':2,'method1': method1})
obj2=Class2() # створити об'єкт obj2
obj2.method1() # викликати метод method1

class My_Type(type): # створити метаклас, який успадковує type
    def __new__(cls, name, bases, dict): # метод створення класу
        return type.__new__(cls, name, bases, dict) # виклик __new__ базового класу
    def __init__(cls, name, bases, dict): # метод ініціалізації класу
        return type.__init__(cls, name, bases, dict) # виклик __init__ базового класу
# створити клас за допомогою метакласу
Class3 = My_Type('Class3', (object,), {'a':3,'method1': method1})
obj3=Class3() # створити об'єкт obj3
obj3.method1() # викликати метод method1
