# -*- coding: utf-8 -*-
"""
## client.py - модуль клієнта
Надсилає дані через мережу серверу з адресою '127.0.0.1' і портом 50007 та отримує їх назад.
"""
import socket
from socketFileIO import write, read
for x in ['A','B','C','End']: # дані, що будуть відсилатись
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # відкрити сокет типу TCP/IP
    s.connect(('127.0.0.1', 50007)) # з'єднати сокет з сервером
    s.sendall(x) # надіслати рядок
    #write(s,x) # або
    x=s.recv(255) # отримати рядок
    #x=read(s) # або 
    print 'Server:', x
    s.close() # закрити сокет
"""
    Server: A
    Server: B
    Server: C
    Server: End
"""
