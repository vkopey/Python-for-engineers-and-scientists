# -*- coding: utf-8 -*-
"""
# pyserial - доступ до послідовного порту
pyserial (http://github.com/pyserial/pyserial) - модуль Python для доступу до послідовного порту на Windows, OSX, Linux, BSD (будь-які POSIX системи) і IronPython. Для тестування віртуальних послідовних портів можна використовувати Eltima Virtual Serial Port Driver (http://www.eltima.com/ru/products/vspdxp) або com0com (http://com0com.sourceforge.net) і створити з'єднані віртуальні порти COM6-COM7. За допомогою Serial Port Terminal можна відкрити COM6 або COM7 для запису чи читання даних. Або можна записувати і читати за допомогою pyserial 2.7, як це показано в прикладі.
"""
import serial,time
data=list("hello!") # дані, що будуть надсилатись
ser6 = serial.Serial(port='COM6', baudrate=9600) # відкрити порт COM6
print ser6.portstr # перевірити чи порт використовується
ser7 = serial.Serial(port='COM7', baudrate=9600) # відкрити порт COM7
print ser7.portstr
x=''
while x!='!': # поки на COM6 не прийде байт '!'
    x=data.pop(0) # отримати і видалити перший елемент
    ser7.write(x) # послати дані з COM7 на COM6
    time.sleep(1) # чекати 1 секунду
    x=ser6.read(1) # читати байт на COM6
    print x,
ser7.close() # закрити порт
ser6.close() # закрити порт
