# -*- coding: utf-8 -*-
"""
# zipfile - робота з ZIP-архівами
Модуль zipfile містить іструменти для створення, читання і запису ZIP-архівів. Приклад створює новий каталог, запаковує його в архів і розпаковує цей архів в інший каталог.
"""
import  zipfile, os
mydir=ur"Каталог"
mydir2=ur"Каталог2"
os.mkdir(mydir); os.mkdir(mydir2) # створити каталоги
zf = zipfile.ZipFile(ur"test_archive.zip", mode='w', compression=zipfile.ZIP_STORED) # відкрити архів для додання без компресії (ZIP_DEFLATED - з компрессією)
for root, dirs, files in os.walk(mydir):
    zf.write(root) # додати в архів каталог
    for file in files: # для кожного файлу
        zf.write(os.path.join(root, file)) # додати в архів файл
zf.close() # закрити файл архіву

zf = zipfile.ZipFile(ur"test_archive.zip", 'r') # відкрити архів для читання
zf.extractall(path=mydir2, members=None, pwd=None) # розпакувати все (підтримуються паролі pwd тільки на розпакування і тільки ZIP2.0)
zf.close() # закрити файл архіву
