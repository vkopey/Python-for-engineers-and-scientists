# -*- coding: utf-8 -*-
"""
# Bokeh - cерверна програма
За допомогою сервера застосувань Bokeh можуть бути створені клієнтські html-документи, які взаємодіють з серверною Python-програмою. Для виконання прикладу введіть в консолі:

    e:/anaconda2/scripts/bokeh serve --show main.py
"""
import numpy as np
from bokeh.io import curdoc
from bokeh.layouts import row, widgetbox
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Slider
from bokeh.plotting import figure
def update(attrname, old, new): # викликається під час прокручування
    y=np.sin(slider.value*x) # нові значення
    source.data=dict(x=x, y=y) # установити нові дані
N = 100 # кількість точок
x = np.linspace(0, 4*np.pi, N)
y = np.sin(x)
source = ColumnDataSource(data=dict(x=x, y=y)) # початкові дані
plot = figure(plot_height=200, plot_width=400, x_range=[0, 4*np.pi], y_range=[-2, 2], output_backend="webgl") # рисунок
plot.line('x', 'y', source=source, line_width=3) # крива
slider = Slider(title="частота", value=1.0, start=0.1, end=3.0, step=0.1) # віджет повзунок
slider.on_change('value', update) # пов'язати подію з функцією
wb = widgetbox(slider) # контейнер з віджетом
curdoc().add_root(row(wb, plot)) # розмістити на документі в ряд
"""
![](fig.png)

Рисунок - GUI програми в браузері
"""
