# -*- coding: utf-8 -*-
"""
# pywin32 - інтерфейс до win32 GUI API
Python for Win32 Extensions (pywin32) -це бібліотека, яка забезпечує доступ до багатьох Windows API з мови Python (http://github.com/mhammond/pywin32). Після установки документація доступна у файлі PyWin32.chm.

Приклад показує можливість застосування pywin32 (версія 221) для управління графічним інтерфейсом інших програм. Програма створює процес calc.exe, знаходить вікно програми і імітує натискання клавіш клавіатури і миші користувачем. Після цього програма входить в цикл, в якому показує відносні координати миші. Щоб завершити програму посуньте курсор миші в верхній лівий кут екрану.
"""
import os, sys, time, win32api, win32gui, win32con
os.system('start calc.exe') # виконати команду і продовжити роботу
time.sleep(1) # чекати 1 секунду
hwnd = win32gui.FindWindow(None, u"Калькулятор") # знайти дескриптор вікна за назвою
try:
    win32gui.SetForegroundWindow(hwnd) # установити на передній план
    cw=win32gui.GetWindowRect(hwnd) # координати вікна
except:
    sys.exit()
for k in [0x32,0x6B,0x33,0x0D]: # натиснути клавіші 2 + 3 Enter
    win32api.keybd_event(k,0,0,0) # k - віртуальний код клавіші
    time.sleep(0.1)
   
win32api.SetCursorPos([cw[0]+380,cw[1]+260]) # установити курсор миші
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0) # натиснути ліву клавішу миші
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0) # відпустити ліву клавішу миші
time.sleep(1)

while True: # цикл
    c=win32gui.GetCursorInfo() # координати курсора миші
    print c[2][0]-cw[0], c[2][1]-cw[1] # відносні координати
    if c[2]==(0,0): break # завершити якщо координати (0,0)