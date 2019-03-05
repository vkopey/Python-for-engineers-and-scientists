# -*- coding: utf-8 -*-
"""
# Контейнери
Контейнер - це структура даних, яка зберігає інші об'єкти в організованому вигляді. Як правило клас контейнера містить методи `__iter__`, `next`, `__getitem__`. Приклад показує створення класу контейнера `Container` і його використання. Див. також модуль `collections`.
"""
class Container(object): # клас контейнера, успадкований від object
    def __init__(self,lst): # конструктор
        self.lst=lst # атрибут-дане список
        self.current=-1 # поточний індекс
    def __iter__(self): # метод повертає ітератор
        return self
    def next(self): # повертає наступний елемент контейнера
        # якщо індекс наступного елемента менший довжини контейнера
        if self.current+1<len(self.lst):
            self.current=self.current+1 # збільшити індекс поточного
            return self.lst[self.current] # повернути поточний
        else: # інакше
            raise StopIteration # генерувати StopIteration
    def __getitem__(self,i): # метод повертає елемент за індексом `i`
        return self.lst[i]
c=Container([1,2,3,4,5]) # створити об'єкт контейнера
for i in c: # для кожного елемента в контейнері
    print i, # вивести його
print
print c[0] # вивести перший елемент (або с.lst[0])
it=iter(c) # створити об'єкт ітератор (або так: c.__iter__())
c.current=0 # установити поточний індекс
print it.next(),it.next(),c[3] # вивести два наступні та четвертий
