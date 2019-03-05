# -*- coding: utf-8 -*-
"""
# scipy.optimize.differential_evolution - диференціальна еволюція
Диференціальна еволюція - це метод глобальної оптимізації функції однієї або багатьох змінних, який відноситься до стохастичних методів оптимізації з границями. Не використовує градієнтні методи, але потребує більшої кількості ітерацій. Моделює такі процеси біологічної еволюції як розмноження, мутація, рекомбінація і відбір. Доступні різні еволюційні стратегії
(http://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.differential_evolution.html). В прикладі шукається мінімум функції $x\sin{x^2}$ в межах [1, 4.5].
"""
import numpy as np
from scipy.optimize import differential_evolution
f=lambda x: x*np.sin(x**2) # функція однієї змінної
res = differential_evolution(f, bounds=[(1, 4.5)]) # знайти мінімум
print res

import matplotlib.pyplot as plt
x=np.linspace(1,5,200)
plt.plot(x,f(x),'k') # графік
plt.scatter(res['x'], res['fun'], linewidths=[3,3]) # мінімум
plt.xlabel('x');plt.ylabel('y');plt.grid();plt.show()
"""
Рисунок - Графік функції і знайдений мінімум в межах [1, 4.5]
"""
