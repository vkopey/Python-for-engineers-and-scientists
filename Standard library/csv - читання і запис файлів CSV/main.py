# -*- coding: utf-8 -*-
"""
# csv - читання і запис файлів CSV
CSV (Comma Separated Values) - це розповсюджений текстовий формат імпорту і експорту електронних таблиць і баз даних (наприклад з Excel). Модуль `csv` реалізує класи для читання і запису табличних даних в форматі CSV.
"""
import csv
csv_file=open("some.csv", "wb") # відкрити файл для запису
writer = csv.writer(csv_file, delimiter = ';') # об'єкт для запису
writer.writerow([0.1,0.2,0.3]) # записати рядок
writer.writerow([0.4,0.5,0.6]) # ще один
csv_file.close() # закрити файл

csv_file=open("some.csv", "rb") # відкрити файл для читання
reader=csv.reader(csv_file,delimiter = ';') # об'єкт для читання
for row in reader:
    print row[0],row[1],row[2]
csv_file.close() # закрити файл
