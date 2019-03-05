# -*- coding: utf-8 -*-
"""
# Matplotlib - процедурний API pyplot
Matplotlib (http://matplotlib.org) є бібліотекою для побудови різноманітних 2D діаграм у різних форматах і для різних інтерактивних середовищ. `matplotlib.pyplot` – це її простий у використанні інтерфейс у стилі MATLAB. Нижче показано приклад створення графіка з лінією між точками (0,0) і (1,1) за допомогою Matplotlib 2.1.1.
"""
import matplotlib.pyplot as plt # імпортувати модуль matplotlib.pyplot як plt
plt.plot([0,1],[0,1], 'o-k') # створити лінію
plt.show() # показати рисунок
"""
Рисунок - Приклад використання matplotlib.pyplot
"""
