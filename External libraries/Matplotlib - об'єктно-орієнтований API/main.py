# -*- coding: utf-8 -*-
"""
# Matplotlib - об'єктно-орієнтований API
Об'єктно-орієнтований інтерфейс програмування Matplotlib використовує об'єкти (таких класів як `figure.Figure`, `axes._subplots.AxesSubplot`, `lines.Line2D`) і їх методи для побудови графіків. Складніший у використанні ніж процедурний інтерфейс pyplot, але має більше можливостей для налаштування графіків.
"""
import matplotlib.pyplot as plt
fig, ax = plt.subplots() # створити об'єкти рисунка і системи координат
#fig, ax = plt.figure(), plt.axes(yscale='log') # або з логарифмічною шкалою 0y
line,=ax.plot([0,2],[0,1]) # створити лінію в системі координат
line.set_linewidth(2) # ширина лінії
line.set_color('r') # колір лінії (або 'red', або (1.0,0.2,0.3), або '0.7')
line.set_linestyle('--') # стиль лінії (або '-', '-.', ':', )
line.set_marker('s') # маркери точок (або один з символів .,ov^<>1234sp*hH+xDd|_)
line.set_markersize(10) # розміри точок
ax.axis('equal') # однаковий масштаб осей
plt.show() # показати рисунок (або fig.show())
"""
Рисунок - Приклад використання об'єктно-орієнтованого API Matplotlib
"""
