#-*- coding: utf-8 -*-
"""
# time - визначення і конвертування значень часу
Функції для визначення і конвертування значень часу. Дивись також модулі `datetime` і `calendar`.
"""
import time
print time.clock() # час CPU в секундах з часу першого запуску цієї функції
time.sleep(1.0) # зупинити виконання на 1 секунду
print time.clock() # буде приблизно 1
print time.time() # кількість секунд з початку Епохи (1.1.1970 р.)
print time.localtime() # поточний час (struct_time)
print time.localtime()[0] # поточний рік
print '*',time.localtime(1424196030) # заданий час (struct_time)
print time.timezone # зона часу як зміщення в секундах
