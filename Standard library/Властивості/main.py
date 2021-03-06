# -*- coding: utf-8 -*-
"""
# Властивості
Властивість - це атрибут, який володіє методами читання, запису і знищення значення. Під час присвоювання властивості значення викликається метод запису, а під час отримання значення властивості - метод читання. Властивості можна створювати в класах, які успадковані від `object`, за допомогою функції `property` або за допомогою декоратора `@property`.
"""
class A(object): # клас A успадкований від object
    __x=0 # приватний атрибут __x
    def getx(self): return self.__x # метод читання
    def setx(self, x): # метод запису
        if x>0: # якщо x>0
             self.__x = x # присвоїти x
        else: self.__x=0 # інакше присвоїти 0
    x = property(getx, setx, None, "Property x") # властивість x з методами читання, запису і рядком документації
a=A() # створити об'єкт класу A
a.x=-2 # присвоїти властивості x значення
print a.x # вивести значення властивості x
