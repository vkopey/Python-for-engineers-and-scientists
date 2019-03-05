# -*- coding: utf-8 -*-
"""
# scipy.optimize.fmin_l_bfgs_b - оптимізація з границями методом L-BFGS-B
Локальна оптимізація векторної функції (двох змінних) популярним квазі-ньютонівським методом L-BFGS-B, який призначений для нелінійних задач з великою кількістю невідомих (http://en.wikipedia.org/wiki/Limited-memory_BFGS). Інтерфейсом для оптимізації функції однієї або багатьох змінних різними методами є `minimize`. В прикладі шукається мінімум функції $y=x_{0}^{2} + x_{1}^{2}$ в межах значень [-5, 5] змінних $x_0$ і $x_1$. 
"""
import numpy as np
from scipy.optimize import minimize, fmin_l_bfgs_b
def f(x): # функція двох змінних
    return x[0]**2+x[1]**2
res=minimize(f, x0=[1.0, 1.0], method="L-BFGS-B", bounds=[(-5,5),(-5,5)])
print res.x
argmin = fmin_l_bfgs_b(f, x0=[1.0, 1.0], bounds=[(-5,5),(-5,5)], approx_grad=True) # або так
print argmin[0]

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
ax=Axes3D(plt.figure()) # система координат
X, Y = np.meshgrid(np.linspace(-5,5), np.linspace(-5,5)); Z=f([X,Y])
ax.plot_wireframe(X, Y, Z) # каркасна поверхня
ax.scatter(res.x[0], res.x[1], res.fun, c='k') # мінімум
ax.set_xlabel('X0'),ax.set_ylabel('X1'),ax.set_zlabel('Y');plt.show()
"""
Рисунок - Графік функції
"""
