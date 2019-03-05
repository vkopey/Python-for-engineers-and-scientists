# -*- coding: utf-8 -*-
"""
# os - файлова система
Модуль os забезпечує переносимий спосіб використання функціональності, пов'язаної з операційною системою. В прикладі показані функції для роботи з файловою системою. Цю програму слід виконувати так:

    python.exe main.py
"""
import os,sys
os.mkdir(r'temp') # створити каталог
with open(r'temp\temp.dat','w') as f:
    f.write('hello\n') # створити файл
print os.path.isdir(r'c:\temp') # чи каталог
print os.path.isfile(r'c:\temp') # чи файл
print os.path.exists(r'temp\temp.dat') # чи існує шлях
print os.path.getsize(r'temp\temp.dat') # розмір в байтах
print os.path.split(r'temp\temp.dat') # розбити на шлях і ім'я
#os.remove(r'temp\temp.dat') # видалити файл
#os.rmdir(r'temp') # видалити каталог
#print os.environ # змінні середовища (можна змінювати)
fd=sys.stdout.fileno() # файловий дискриптор (1)
os.write(fd,'hello\n') # запис в стандартний потік як у файл
print os.getcwd() # поточний каталог
os.chdir(r'temp') # змінити поточний каталог
cwd=os.getcwdu() # поточний каталог (unicode рядок)
print os.listdir(cwd) # список елементів каталогу
for root, dirs, files in os.walk(cwd): # або за допомогою генератора os.walk
    print root, dirs, files
