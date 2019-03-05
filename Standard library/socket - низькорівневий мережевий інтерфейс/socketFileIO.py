# -*- coding: utf-8 -*-
"""
## socketFileIO.py - читання і запис об'єктів Python через сокет
Нижче наведено код модуля `socketFileIO.py` з функціями `write` і `read`, які дозволяють відсилати чи отримувати об'єкти Python по мережі через сокети. В модулях `server.py` і `client.py` розкоментуйте виклики цих функцій і закоментуйте виклики `sendall` та `recv`. 
"""
import pickle

def write(soc, obj):
    "Відсилає об'єкт obj через сокет soc"
    f = soc.makefile('wb') # створити файл, асоційований з сокетом
    pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL) # серіалізувати obj в файлі
    f.close() # закрити файл

def read(soc):
    "Повертає об'єкт, отриманий з сокета soc"
    f = soc.makefile('rb') # створити файл, асоційований з сокетом
    obj = pickle.load(f) # десеріалізувати obj з файлу
    f.close() # закрити файл
    return obj
