# -*- coding: utf-8 -*-
"""
# concurrent.futures - запуск паралельних задач
concurrent.futures - високорівневий інтерфейс для асинхронного виконання виконуваних об'єктів за допомогою потоків (`ThreadPoolExecutor`) або процесів (`ProcessPoolExecutor`). Входить в стандартну бібліотеку Python 3.2, але доступний і для Python 2.7 (http://pypi.org/project/futures). Подібний приклад можна також розробити за допомогою multiprocessing. Див. також приклад використання інтерфейсу futures в розподілених обчисленнях (Dask.Distributed).
"""
import concurrent.futures, time
def f(x): # функція, яка буде виконуватись в окремих процесах
    time.sleep(x) # затримка (тільки для тестування паралельності)
    return x
if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as e:
        a=e.submit(f, 4) # виконати в окремому процесі f(x=4)
        b=e.submit(f, 2)
        c=e.submit(f, 3)
        d=e.submit(f, 1)
        # для кожного об'єкта Future, що виконує f
        for fut in concurrent.futures.as_completed([a,b,c,d]):
            print fut.result(), # отримати результати асинхронно
        #print [x.result() for x in [a,b,c,d]] # або чекати усі результати
        #print [x for x in e.map(f, [1,2,3,4])] # або простіше
"""
    1 2 3 4
"""
