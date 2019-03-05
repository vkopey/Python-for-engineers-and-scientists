# -*- coding: utf-8 -*-
"""
# Bokeh - інтерактивна візуалізація
Bokeh 0.13 (http://bokeh.pydata.org) - це бібліотека для інтерактивної і високопродуктивної візуалізації в сучасних браузерах. Використовується для створення інтерактивних програм для візуалізації даних. Цей приклад створює графік, який розташований в незалежному html-документі з javascript-сценаріями.
"""
import numpy as np
from bokeh.plotting import figure, show, output_file
x = np.linspace(-1,1,1000) # дані для візуалізації
y = np.sin(1/x)
dy= np.random.normal(0, 0.2, len(x))
output_file("plot.html") # документ для виведення
plot = figure(plot_height=200, output_backend="webgl") # рисунок
plot.line(x, y, line_width=3) # крива
plot.circle(x[::100], y[::100], fill_color="white", line_color="red", size=10) # точки на кривій
plot.scatter(x, y+dy, alpha=0.5) # випадкові точки
show(plot) # показати рисунок в браузері
"""
![](fig.png)

Рисунок - Вигляд графіка в браузері
"""
