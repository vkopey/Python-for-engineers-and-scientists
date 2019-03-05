# -*- coding: utf-8 -*-
"""
# Взаємодія з Maple 
Maple (http://www.maplesoft.com) - система комп'ютерної математики з можливостями символьних обчислень. У прикладі показано спосіб взаємодії Python з Maple шляхом створення файлу `mymaple.mpl` з командами Maple та командного файлу `mymaple.bat`, який створює процес `cmaple.exe`, що виконує ці команди і повертає файл результатів `result.txt`.
"""
import os
f=open("d:/mymaple.mpl", "w") # відкрити файл з командами Maple для запису
f.write(r"evalf(sin(Pi/3));") # записати в файл команду Maple
f.close() # закрити файл
f=open("d:/mymaple.bat", "w") # відкрити командний файл для запису
f.writelines((r"path d:\Program Files\Maple 14\bin.win"+"\n",
              r"cmaple.exe < d:\mymaple.mpl > d:\result.txt"+"\n",
              r"exit")) # записати команди в командний файл
f.close() # закрити файл
print os.system(r'start /WAIT d:\mymaple.bat') # виконати команду ОС і чекати її завершення
os.remove(r"d:\mymaple.bat") # видалити файл
os.remove(r"d:\mymaple.mpl")
