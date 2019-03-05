# -*- coding: utf-8 -*-
"""
# Dask.Distributed - розподілені обчислення
Розподілені обчислення - це вид паралельних обчислень за допомогою множини комп'ютерів, які об'єднані в мережу. Dask.Distributed (http://distributed.readthedocs.io) - це легка бібліотека для розподілених обчислень на Python. Вона розширює API `concurrent.futures` і `Dask` (бібліотека паралельних обчислень на чистій Python) для невеликих кластерів. Для виконання прикладу необхідно установити Dask повністю на кожній Windows машині:

    pip install "dask[complete]"
Або на Linux-машині:

    sudo pip2 install "dask[complete]"
На одній машині (наприклад 192.168.1.33) запустити планувальник:

    dask-scheduler
На кожній машині запустити виконавців, які виконують завдання планувальника за допомогою ThreadPool. Якщо обчислення вивільняють GIL (наприклад NumPy або Pandas), введіть:

    dask-worker 192.168.1.33:8786
Або, якщо обчислення не вивільняють GIL:

    dask-worker 192.168.1.33:8786 --nprocs 4 --nthreads 1
Виконати програму клієнта:

    python main.py
Переглянути статус виконання можна в браузері (потрібен установлений Bokeh):

    http://192.168.1.33:8787
"""
from dask.distributed import Client, as_completed
import time
def f(x): # функція, яка буде виконуватись в окремих процесах
    time.sleep(x)
    return x
if __name__ == '__main__':
    #client = Client() # клієнт (кластер на локальній машині)
    client = Client('192.168.1.33:8786') # клієнт 
    print client
    a=client.submit(f, 4) # виконати на кластері f(x=4)
    b=client.submit(f, 2)
    c=client.submit(f, 3)
    d=client.submit(f, 1)
    # для кожного об'єкта Future, що виконує f
    for fut in as_completed([a,b,c,d]):
        print fut.result(), # отримати результати асинхронно
    #futures=client.map(f, [1,2,3,4,5,6,7,8]) # або
    #print client.gather(futures)  # чекати усі результати
    # або [fut.result() for fut in futures]
"""
    <Client: scheduler='tcp://192.168.1.33:8786' processes=8 cores=8>
    1, 2, 3, 4
"""
