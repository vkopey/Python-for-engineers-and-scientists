# -*- coding: utf-8 -*-
"""
# inspect - перегляд об'єктів часу виконання
Модуль inspect містить додаткові функції, які допомагають отримати інформацію про об’єкти часу виконання (модулі, класи, методи, функції, об'єкти трасування, кадрів виконання і коду).
"""
import inspect
# клас A
class A(): pass
print inspect.getmro(A) # кортеж з ієрархією базових класів
print inspect.getmembers(A) # повертає список пар (ім'я, значення) членів об'єкта 
print inspect.getcomments(A) # коментар перед класом A
#print inspect.getsource(A) # текст вихідного коду класу A
print inspect.isclass(A) # чи A є класом?

def f(a,b=0,*args,**kwargs):
    cf=inspect.currentframe() # об'єкт поточного кадру виконання
    #cf=sys._getframe() # або
    #cf.f_back # попередній кадр стеку (який викликав f)
    print cf.f_lineno, cf.f_back.f_lineno # поточний рядок коду і рядок, який викликав f
    print cf.f_locals # локальні імена f
    #print cf.f_back.f_code.co_filename # файл модуля, що викликав f

print inspect.ismethod(f) # чи f є методом?
print inspect.isfunction(f) # чи f є функцією?
print inspect.getargspec(f) # імена аргументів функції
f(1,2,3,x=4) # виклик функції
