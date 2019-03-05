# -*- coding: utf-8 -*-
"""
# Matplotlib - інтерактивна побудова графіків
В прикладі графік інтерактивно перебудовується під час натиску клавіш "стрілка вгору" і "стрілка вниз". Для цього подія `key_press_event` пов'язується з функцією обробки події `keyPress`. Цю програму бажано виконувати так: python.exe main.py
"""
import matplotlib.pyplot as plt
from random import randint

def keyPress(event): # функція обробки подій
    if event.key=='up': # якщо натиснута стрілка вгору
        X.append(randint(0,10)) # додати в список X випадкове число
        Y.append(randint(0,10)) # додати в список Y випадкове число
    if event.key=='down': # якщо натиснута стрілка вниз
        if X: X.pop() # вилучити зі списку X останнє число
        if Y: Y.pop() # вилучити зі списку Y останнє число
    ln.set_data(X,Y) # установити дані для полілінії
    plt.draw() #ln.figure.canvas.draw() # перерисувати

X=[] # список координат x
Y=[] # список координат y
ln,=plt.plot(X, Y, 'k-o') # полілінія
plt.gcf().canvas.mpl_connect('key_press_event', keyPress) # пов'язати подію натиску клавіш з функцією обробки подій
plt.axis([0, 10, 0, 10]) # шкала осей
plt.xlabel("x");plt.ylabel("y");plt.show()
"""
Рисунок - Інтерактивний графік
"""
