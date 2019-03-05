# -*- coding: utf-8 -*-
"""
# xlwt - створення електронних таблиць Excel
xlwt (http://pypi.org/project/xlwt) - бібліотека для створення електронних таблиць у форматі  Microsoft Excel 95-2003 на будь-якій платформі. В прикладі за допомогою xlwt 1.3.0 створюється робоча книга і лист Excel, в комірки якого заноситься значення і формула.
"""
import xlwt
workbook = xlwt.Workbook() # робоча книга Excel
sheet = workbook.add_sheet("Sheet1") # робочий лист
sheet.write(0, 0, 7.0) # записати в комірку 0, 0 значення
sheet.write(0, 1, xlwt.Formula("A1+2")) # записати в комірку 0, 1 формулу 
workbook.save("Book1.xls") # зберегти файл
