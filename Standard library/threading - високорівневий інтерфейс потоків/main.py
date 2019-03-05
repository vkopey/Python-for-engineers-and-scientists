# -*- coding: utf-8 -*-
"""
# threading - високорівневий інтерфейс потоків
Цей модуль створює високорівневі інтерфейси потоків на основі низькорівневого модуля `thread`. Потоки описуються нащадком класу `threading.Thread`, а їх активність - перевизначеним методом `run`. В прикладі створюються 4 потоки, які виконуюють код в методі `run`. Звернення потоків до спільного списку `A` синхронізовано за допомогою простого об'єкта блокування `threading.Lock`. Нижче показані результати роботи програми з цим об'єктом і без нього. Додатково створюється потік, який стартує через 2 секунди і додає в список `A` рядок 'timer'.
"""
import threading, time

class Thread(threading.Thread): # успадкований від threading.Thread
    def __init__(self, i): # конструктор
        self.i=i # ідентифікатор потоку
        threading.Thread.__init__(self) # виклик конструктора базового класу   
    def run(self): # забезпечує логіку потоку
        mutex.acquire() # блокувати (лише один потік може виконуватись в один і той самий момент часу)
        #semaphore.acquire() # або так
        A.append(self.i)
        time.sleep(1)
        A.append(self.i)
        mutex.release() # розблокувати
        #semaphore.release() # або так

mutex = threading.Lock() # те саме що thread.allocate_lock()
#semaphore=threading.Semaphore(1) # або семафор (тільки 1 потік одночасно)
A=[] # глобальний список
T=[] # список потоків
for i in range(4): # створити 4 потоки
    t=Thread(i) # створити потік
    t.start() # виконати метод run в потоці
    T.append(t) # додати в список потоків
t = threading.Timer(2.0, lambda: A.append('timer')) # створити потік,
t.start() # який стартує через 2 с
T.append(t)
for t in T:
    t.join() # поки усі потоки не приєднаються
print A
