# -*- coding: utf-8 -*-
"""
# SocketServer - каркас для мережевих серверів
Високорівневий модуль `SocketServer` спрощує задачі створення мережевих серверів. Для створення власного обробника мережевих запитів потрібно успадкувати клас `BaseRequestHandler` і перевизначити метод `handle`. В прикладі на основі `SocketServer` створено багатопотоковий сервер з адресою '127.0.0.1' і портом 50007. Сервер отримує дані через мережу від клієнтів та відсилає їх назад. Для тестування багатопотоковості запустіть цей сервер `python serverT.py` і кілька клієнтів `python client.py`. В диспетчері завдань Windows 7 можна побачити, як змінюється кількість потоків процесу сервера.
"""
import SocketServer, time
from socketFileIO import write, read  # якщо потрібно

class MyClientHandler(SocketServer.BaseRequestHandler): # клас обробника запитів
    def handle(self): # обробляє запити (перевизначений)
        print self.client_address # показати адресу клієнта
        x=self.request.recv(255) # отримати рядок
        #x=read(self.request) # або
        print 'Client:', x
        time.sleep(10) # затримка (для тестування багатопотоковості)
        self.request.sendall(x) # надіслати рядок
        #write(self.request,x) # або
        self.request.close() # закрити з'єднання з клієнтом

# створити багатопотоковий TCP сервер з обробником MyClientHandler
server = SocketServer.ThreadingTCPServer(('', 50007), MyClientHandler) # порт 50007 або порт 0 (довільний незайнятий порт)
try:
    server.serve_forever() # обробляти запити вічно
except KeyboardInterrupt: # якщо натиснуто Ctrl-C
    server.shutdown() # зупинити сервер
