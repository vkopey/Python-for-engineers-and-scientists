# -*- coding: utf-8 -*-
"""
# Статичні методи та методи класу
Статичний метод - це функція, яка визначена в класі, але не належить класу чи екземпляру. Метод класу - це метод, який належить класу, а не екземпляру. Метод класу має перший аргумент `cls` (клас), а не `self` (екземпляр). Статичні методи і методи класу визначаються за допомогою декораторів `@staticmethod` і `@classmethod`.
"""
class A: # визначення класу A
    a=0 # атрибут класу
    def f(self, x): # метод екземпляра
        return self.a+x
    @staticmethod # декоратор
    def f2(x): # статичний метод
        return 1+x
    @classmethod # декоратор
    def f3(cls, x): # метод класу
        return cls.a+x
obj=A() # створити об'єкт (екземпляр)
obj.a=2 # атрибут екземпляра (не класу!)
print obj.f(1) # виклик методу екземпляра
print A.f(obj, 1) # або
print A.f2(1) # виклик статичного методу
print A.f3(1) # виклик методу класу
