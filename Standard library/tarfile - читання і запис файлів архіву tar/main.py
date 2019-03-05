# -*- coding: utf-8 -*-
"""
# tarfile - читання і запис файлів архіву tar
Модуль `tarfile` дозволяє читати і записувати tar-архіви з підтримкою стиснення даних gzip або bz2. Приклад створює новий каталог, запаковує його в архів і розпаковує цей архів в інший каталог.
"""
import tarfile, sys, os
encoding=sys.getfilesystemencoding() # кодування в файловій системі (у Windows 7 - mbcs)
mydir=ur"Каталог"
mydir2=ur"Каталог2"
os.mkdir(mydir); os.mkdir(mydir2) # створити каталоги
tar = tarfile.open(ur"test_archive.tar", mode='a', format=tarfile.PAX_FORMAT) # відкрити архів для додання
tar.add(mydir) # додати в архів
tar.close() # закрити файл архіву

tar = tarfile.open(ur"test_archive.tar", mode='r', format=tarfile.PAX_FORMAT) # відкрити архів для читання
tar.extractall(path=mydir2.encode(encoding), members=None) # розпакувати все
for x in tar.getmembers(): # для кожного елемента архіву
    print x.name.decode(encoding) # вивести його ім'я
    print x.size # розмір в байтах
    print x.mtime # час останньої модифікації
    print x.isdir() # чи це каталог?
tar.close() # закрити файл архіву
