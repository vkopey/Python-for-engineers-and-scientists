# -*- coding: utf-8 -*-
"""
# Оператор умови if
Інструкція `if` виконує певні команди тоді, коли значення логічного виразу рівне `True` (істина). Інструкція `if` може застосовуватись з `elif` та/або `else`. Якщо значення логічного виразу після `if` рівне `False` (не істина), то виконується інструкція `elif`, або, якщо її немає, виконується `else`. Послідовних інструкцій `elif` може бути довільна кількість.
"""
x = 2 # присвоїти x 2
if x<0: # якщо x<0 то
    y=1 # присвоїти y 1
    print "x<0, y=",y # вивести на екран
elif x>1 or x==0: # інакше, якщо x>0 або x=0 то
    y=2 # присвоїти y 2
    print "x>0, y=",y # вивести на екран
else: # інакше
    y=0 # присвоїти y 0
    print "x=0, y=",y # вивести на екран
