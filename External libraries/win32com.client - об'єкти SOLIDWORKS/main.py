# -*- coding: utf-8 -*-
"""
# win32com.client - об'єкти SOLIDWORKS
В прикладі створюється клієнт COM для доступу до об'єктів системи автоматизованого проектування SOLIDWORKS. Програма змінює значення розміру активної моделі і перебудовує модель.
"""
import win32com.client
swApp = win32com.client.Dispatch("SldWorks.Application") # створити об'єкт SldWorks.Application
Part=swApp.ActiveDoc # активний документ
# змінити значення параметра "D1@Extrude1" на 10 мм
Part.Parameter("D1@Extrude1").SystemValue = 10.0/1000
Part.EditRebuild # перебудувати модель
