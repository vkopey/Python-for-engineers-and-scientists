# -*- coding: utf-8 -*-
"""
# multiprocessing - запуск паралельних задач
Аналог прикладу concurrent.futures на основі multiprocessing. Тут функціям `ProcessPoolExecutor`, `submit`, `result`, `map` відповідають `Pool`, `apply_async`, `get`, `map`.
"""
import time
from multiprocessing import Pool
def f(x): # функція, яка буде виконуватись в окремих процесах
    time.sleep(x) # затримка (тільки для тестування паралельності)
    return x
if __name__ == '__main__':
    pool = Pool() # пул процесів
    a = pool.apply_async(f, [4]) # AsyncResult
    b = pool.apply_async(f, [2])
    while any([a,b]): # отримати результати асинхронно
        if a and a.ready(): print a.get(); a=False 
        if b and b.ready(): print b.get(); b=False
    #print pool.map(f, [1,2]) # або чекати усі результати
