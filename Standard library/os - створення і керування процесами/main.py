# -*- coding: utf-8 -*-
"""
# os - створення і керування процесами
В цьому прикладі показані функції модуля os для створення і керування процесами. Ознайомтесь також з більш новим модулем subprocess.
"""
import os
print os.getpid() # ідентифікатор процесу
os.system(r'start calc.exe') # виконує команду оболонки
print os.system(r'echo hello') # виконує команду оболонки
print os.popen(r'echo world').read() # читати результати команди оболонки
id = os.spawnv(os.P_NOWAIT, 'c:\\Windows\\Notepad.exe',[r' c:\Python27\README.txt']) # виконує програму без очікування виходу з неї
status = os.waitpid(id, 0) # але тут чекає завершення процесу id
print 'status=', status
os.startfile(r'c:\Python27\README.txt') # виконує файл відповідним застосуванням
os.execl(r'c:\Windows\Notepad.exe', ' c:\Python27\README.txt') # виконує файл, замінює поточний процес
print "hello" # ця команда вже не виконається
