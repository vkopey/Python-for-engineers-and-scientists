# -*- coding: utf-8 -*-
"""
# win32com.client - об'єкти Excel з обробкою подій
В більш складному прикладі створюється клієнт COM для доступу до об'єктів Excel з обробкою подій. Під час оброблення події програми `OnSheetBeforeDoubleClick` та події робочого листа `OnSelectionChange` виводиться інформація про вибрані комірки. Цей модуль слід виконувати так:

    python main.py

Для виходу слід в консолі натиснути Esc. Дивись інші приклади в `c:\Python27\Lib\site-packages\win32com\test`.
"""
import win32com.client
import msvcrt, pythoncom

class MyExcelEvents: # події прикладної програми Excel
    def OnSheetBeforeDoubleClick(self, Sheet, Target, Cancel): # обробник події OnSheetBeforeDoubleClick
        print "SheetBeforeDoubleClick"
        print Target.GetAddress() # Target - комірка
        print Target.Column # колонка
        print Target.Row # рядок
        #Target.Value='111' # значення комірки
        
class MyWorksheetEvents(): # події робочого листа Worksheet
    def OnSelectionChange(self,Range): # обробник події OnSelectionChange
        print dir(Range)[:3] # вивести деякі атрибути об'єкта Range (діапазон комірок)
        print Range.GetAddress() # отримати адресу комірки
        print Range.GetValue() # отримати значення комірки
        
excelApp = win32com.client.DispatchWithEvents("Excel.Application",  MyExcelEvents) # створити об'єкт Excel.Application з обробкою подій
#excelApp = win32com.client.Dispatch("Excel.Application") # без обробки подій

excelApp.Visible = 1 # зробити Excel видимим
workBook=excelApp.Workbooks.Add() # додати робочу книгу

workSheet=excelApp.ActiveWorkbook.ActiveSheet # активний лист
workSheet=win32com.client.DispatchWithEvents(workSheet, MyWorksheetEvents) # створити об'єкт workSheet з обробкою подій 

workSheet.Cells(1,1).Value = 100 # в комірку 1,1 помістити 100
# в діапазони комірок помістити значення:
workSheet.Range("B1:D2").Value =((1,2,3),(10,20,30))
workSheet.Range("B3:D3").Value =(u"а",u"б",u"в")
workSheet.Range("A2").Value = "=A1+1"
# або workSheet.Cells(2,1).Formula = "=A1+1"

while True: # цикл
    if msvcrt.kbhit(): # якщо в консолі натиснута клавіша
        if ord(msvcrt.getch())==27: break # завершити, якщо це Esc
    pythoncom.PumpWaitingMessages() # обробляти події

workBook.Close(False) # закрити робочу книгу без збереження
excelApp.Quit() # вийти з Excel

excelApp=workBook=workSheet=None
from win32com.test.util import CheckClean
CheckClean() # перевірити скільки COM об'єктів залишилося
pythoncom.CoUninitialize() # відмінити ініціалізацю
CheckClean() # перевірити скільки COM об'єктів залишилося
"""
    SheetBeforeDoubleClick
    $A$1
    1
    1
    ['Activate', 'AddComment', 'AdvancedFilter']
    $A$2
    101.0
![](fig.png)

Рисунок - Робочий лист Excel
"""
