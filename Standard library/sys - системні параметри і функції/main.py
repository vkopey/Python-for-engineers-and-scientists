# -*- coding: utf-8 -*-
"""
# sys - системні параметри і функції
Модуль sys містить змінні та функції, які мають відношення до інтерпретатора Python та його середовища.
"""
import sys
print sys.platform # платформа
print sys.version # версія інтерпретатора
print sys.argv # аргументи командного рядка
sys.builtin_module_names # вбудовані модулі
sys.modules # модулі що завантажуються
print sys.getsizeof(int()) # розмір об'єкта в байтах
sys.path # шлях до пошуку модулів
#sys.path.append('D:\\') # додати шлях пошуку модулів
#print sys.stdin.readline() # читати рядок з стандартного потоку введення (тут програма буде чекати введення)
print sys.stdin.isatty() # чи стандартний потік є консоллю
sys.stdout.write("hello stdout\n") # запис в стандартний потік виведення
sys.stdout=open('temp.dat','w') # перенаправлення виведення у файл
print "hello file" # виведення у файл
sys.stdout=sys.__stdout__ # відміна перенаправлення
print "hello console" # виведення знову на консоль
try: raise IndexError # генерувати виняткову ситуацію
except: print sys.exc_info() # інформація про виняткову ситуацію
#sys.exit() # завершення програми
