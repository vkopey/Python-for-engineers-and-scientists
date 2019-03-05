# -*- coding: utf-8 -*-
"""
# multiprocessing - підтримка багатох процесів
multiprocessing - це пакет, який підтримує створення процесів з використанням API, який подібний на API модуля threading. Забезпечує локальний і віддалений паралелізм, ефективно долає GIL шляхом використання підпроцесів замість потоків. В приклад розпаралелюється задача знаходження квадратів 50 матриць 1000x1000 за допомогою класу `Poll` і його методу `map`. Зауважте, що виграш в продуктивності буде досягнуто тільки на багатопроцесорній системі. Виконайте програму послідовно в паралельному і звичайному режимах так:

    python main.py
    python main.py s

Для визначення продуктивності програми використано модуль `timeit`. В Windows можна також використати команду:
    
    echo %time% & main.py & call echo %^time%
"""
import numpy as np 
from multiprocessing import Pool # задіяти багато процесів
#from multiprocessing.dummy import Pool # або задіяти багато потоків
import sys, timeit
def f(x): # функція, яка виконується в кожному процесі
    return x*x
if __name__ == '__main__':
    time = timeit.default_timer()
    X=[np.matrix(np.random.rand(1000,1000)) for i in range(50)] # 50 матриць 1000x1000
    if 's' in sys.argv:
        Y=map(f,X) # застосувати f для кожного у X (тільки 1 процес)
    else:
        p=Pool(4) # створити пул 4-х процесів
        Y=p.map(f, X) # задіяти 4 процеси
    print timeit.default_timer() - time
