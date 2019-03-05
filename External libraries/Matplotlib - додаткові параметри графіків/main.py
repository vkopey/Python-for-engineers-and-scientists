# -*- coding: utf-8 -*-
"""
# Matplotlib - додаткові параметри графіків
В прикладі показно створення вкладених графіків (subplot) і використання їх додаткових параметрів, таких як назви і масштаб осей, заголовок, сітка, надписи. Можливо налаштувати деякі параметри за замовчування в словнику `plt.rcParams`.
"""
import numpy as np # імпортувати модуль numpy як np
import matplotlib.pyplot as plt # імпортувати модуль matplotlib.pyplot як plt
# параметри графіків за замовчуванням:
plt.rcParams['lines.color'] = 'k'
#plt.rcParams['image.aspect'] = 'equal' # але це не працює у версії 2.1.1
#plt.rcParams.keys() # список усіх параметрів

f=lambda x: np.cos(np.pi*x)*x # функція повертає x*cos(pi*x)
x1 = np.arange(0.0, 5.0, 0.1) # масив з прогресії
x2= np.arange(0.0, 5.0, 0.02) # масив з прогресії
plt.subplot(2,1,1) #діаграма 1 (рядків 2, колонок 1, номер 1)
plt.plot(x1,f(x1),'bo',x2,f(x2),'k') # криві
plt.title('Figure1') # заголовок
plt.subplot(2,1,2) # діаграма 2 (рядків 2, колонок 1, номер 2)
line1,line2=plt.plot([1,2,3],[2,4,8],'r-',[1,2,3],[1,2,1],'b-') # криві line1,line2
line3,=plt.plot([1,2,3],[1.5,3,4.5],'g--') # крива line3
plt.setp((line1,line2),linewidth=2.0) # властивості кривих line1,line2
plt.title('Figure2') # заголовок
plt.xlabel('x'); plt.ylabel('y') # надпис осей x і y
plt.text(2, 2, r'$\sigma=2/6$') # LaTeX текст на діаграмі
plt.axis([1, 3, 0, 10]) # розміри осей x,y
# plt.axis('equal') # однаковий масштаб осей
plt.grid(True) # сітка
plt.show() # показати графік
"""
Рисунок - Створення вкладених графіків
"""
