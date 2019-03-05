# -*- coding: utf-8 -*-
"""
## server.py - модуль сервера
Модуль отримує дані від клієнта через stdin та відсилає їх назад через stdout.
"""
import pickle,sys
# ! тут заборонено використовувати print
s=sys.stdin.read().decode("string_escape") # перетворити з рядкового літералу Python
data = pickle.loads(s) # перетворити в список
data.append('D') # додати дані
s=pickle.dumps(data) # серіалізувати список в рядок
s=s.encode("string_escape") # перетворити в рядковий літерал Python (без "\n")
sys.stdout.write(s) # записати в stdout
