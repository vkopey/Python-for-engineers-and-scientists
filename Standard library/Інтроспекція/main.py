# -*- coding: utf-8 -*-
"""
# Інтроспекція
Інтроспекція в Python - це можливість отримати всю інформацію про структуру будь-якого об'єкта під час виконання. Найбільш відомим засобом для інтроспекції в Python є функція `dir`, яка повертає список імен атрибутів переданого їй об’єкта. Функція `type` або атрибут `__class__` дозволяють отримати тип об’єкта. Функція `vars` або атрибут `__dict__` дозволяють отримати словник з парами атрибут:значення об’єкта. Функції `hasattr`, `getattr` і `setattr` дозволяють відповідно перевірити наявність у об’єкта заданого атрибута, повернути його і змінити значення. Функція `issubclass` дає змогу визначити чи успадковується один клас від іншого, а метод `__subclasses__` повертає список підкласів. Кортеж базових класів та їх ієрархію можна отримати за допомогою атрибутів `__bases__` і `__mro__`.
"""
class A(object): # успадкований від object клас A
    '''Клас A''' # рядок документації
    def __init__(self,a): # конструктор
        self.a=a # атрибут a
    def f(self): # метод f
        '''Повертає self.a''' # рядок документації
        return self.a
class B(A): # успадкований від A клас B
    '''Клас B''' # рядок документації
    def __init__(self,a,b): # конструктор
        super(B, self).__init__(a) # виклик конструктора базового класу
        self.b=b # атрибут b
    def f(self): # метод f
        '''Повертає суму self.a+self.b''' # рядок документації
        return self.a+self.b

obj=B(0,2) # створення об'єкта класу B, виклик конструктора
obj.a=1 # зміна значення атрибута a
obj.f() # виклик методу f

print dir(B) # список імен атрибутів класу B
print dir(obj) # список імен атрибутів об'єкта obj
print id(obj) # унікальний ідентифікатор об'єкта
print obj.__sizeof__() # розмір об'єкта в пам'яті в байтах 
print B.__doc__ # рядок документації класу B
print obj.f.__doc__ # рядок документації методу f
print B.__name__ #  ім'я класу B
print __name__ # ім'я модуля
print type(obj) # тип (клас) об'єкта obj
# або obj.__class__
print obj.__class__.__name__ # ім'я типу об'єкта obj
print vars(obj) # словник з парами атрибут:значення
# або obj.__dict__
print hasattr(obj, 'a') # чи є атрибут 'a' у об'єкта obj?
setattr(obj, 'a', 3) # зміна значення (3) атрибута 'a' об'єкта obj
# або obj.__setattr__('a',3)
print getattr(obj, 'a') # значення атрибута 'a' об'єкта obj
# або obj.__getattribute__('a')
# або obj.__dict__['a']
print callable(obj.f) # чи атрибут f є методом?
print isinstance(obj, B) # чи obj є екземпляром B?
print issubclass(A, object) # чи A є підкласом object?
print A.__subclasses__() # підкласи A 
print B.__bases__ # кортеж базових класів
print B.__mro__ # кортеж з ієрархією базових класів
