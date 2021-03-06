# -*- coding: utf-8 -*-
"""
# Декоратори класу
За тим самим принципом можна обгортати класи. Приклад показує як за допомогою декоратора класу автоматично змінювати значення його атрибута `__name__`.
"""
def decorator(arg): # функція отримує аргумент і повертає внутрішню функцію f
    def f(cls): # внутрішня функція-обгортка отримує і повертає клас
        cls.__name__=arg # змінити значення атрибута класу
        return cls # повертає клас
    return f
# застосування декоратора класу з аргументом
@decorator('Мій клас')
class A(object): # клас
    a=1
print A.__name__
