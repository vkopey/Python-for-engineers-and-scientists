# -*- coding: utf-8 -*-
"""
# subprocess - керування підпроцесами
Процес - це об'єкт операційної системи, який описує програму, що виконується. Процес є контейнером, який містить такі ресурси як ідентифікатор процесу, образ виконуваного машинного коду програми, пам'ять, дескриптори ресурсів ОС, атрибути безпеки, стан процесора, потоки процесу. Модуль subprocess дозволяє створювати нові процеси, під'єднуватись до їх input/output/error каналів та отримувати їхні коди завершення. Цей модуль призначений для заміни кількох старих модулів і функцій (`os.system, os.spawn*, os.popen*, popen2.*, commands.*`).
"""
import subprocess
p=subprocess.Popen(['notepad', r'c:\Python27\README.txt']) # повертає об'єкт Popen, який являє собою новий процес
print p.wait() # чекає його завершення, повертає код завершення

#print subprocess.call(r'notepad c:\Python27\README.txt') # те саме
print subprocess.call('ver', shell=True) # те саме в консолі
print subprocess.check_output('python -c "x=1\nprint x"') # виконує команду і повертає її виведення
# або
p = subprocess.Popen('python -c "print 1+1"', stdout=subprocess.PIPE)
print p.stdout.read()

p = subprocess.Popen('python', stdin=subprocess.PIPE,
stdout=subprocess.PIPE, stderr=subprocess.PIPE) # новий процес
out, err = p.communicate("print 1+2") # посилає дані в stdin процесу
print out, err # і читає дані з stdout і stderr
