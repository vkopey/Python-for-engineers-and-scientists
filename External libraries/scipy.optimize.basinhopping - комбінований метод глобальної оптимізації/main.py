# -*- coding: utf-8 -*-
"""
# scipy.optimize.basinhopping - комбінований метод глобальної оптимізації
Функція `scipy.optimize.basinhopping` реалізує комбінований метод глобальної багатомірної оптимізації. В кожній ітерації є етапи:

1. Випадкове збурення координат.
2. Локальна мінімізація.
3. Прийняття або відхилення нових координати, основане на мінімізованому значенні функції.

Метод не гарантує знаходження мінімуму, оскільки алгоритм стохастичний. Алгоритм має багато параметрів, серед яких:

- `x0` - початкові значення мінімумів;
- `niter` - кількість ітерацій алгоритму;
- `T` - параметр для прийняття чи відхилення критерію;
- `stepsize` - початковий розмір кроку для випадкових зміщень;
- `minimizer_kwargs` - аргументи, які передаються локальному мінімізатору. Для пришвидшення можна також передавати мінімізатору похідні функції (Якобіан, Гессіан);
- `take_step` - замінює функцію кроку за замовчуванням;
- `accept_test` - визначає тест, який використовується для прийняття або відхилення кроку;
- `callback` - функція, яка викликається, коли знайдено локальний мінімум.

"""
import numpy as np
from scipy.optimize import basinhopping

def f(x): # функція двох змінних
    y = np.cos(14.5*x[0]-0.3)+(x[1]+0.2)*x[1]+(x[0]+0.2)*x[0]
    #y=1 + 2*x[0] + 2*x[1] # (тільки для тестування accept_test. Див. нижче)
    return y # для пришвидшення пошуку мінімуму функція разом зі значенням може також повертати градієнт (див. документацію)   

ret = basinhopping(func=f, x0=[0.0, 0.0]) # знайти мінімум
print ret['x'], ret['fun']

class MyBounds(object): # реалізує границі проблеми
    def __init__(self, xmax=[1.1, 1.1], xmin=[-1.1, -1.1] ):
        self.xmax = np.array(xmax) # максимум для x
        self.xmin = np.array(xmin) # мінімум для x
    def __call__(self, **kwargs):
        x = kwargs["x_new"]
        tmax = bool(np.all(x <= self.xmax)) # True, якщо x менше рівне максимуму
        tmin = bool(np.all(x >= self.xmin)) # True, якщо x більше рівне мінімуму
        return tmax and tmin # якщо False (за границями), то мінімум не приймається

def print_fun(x, f, accepted): # викликається, коли знайдено лок. мінімум
    print "Loc. min.", x, f, accepted # координати, значення функції, чи мінімум приймається

ret = basinhopping(func=f, x0=[0.0, 0.0], niter=5, stepsize=0.1, minimizer_kwargs = {"method": "L-BFGS-B"}, accept_test=MyBounds(), callback=print_fun) # знайти мінімум
print ret['x'], ret['fun']

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
ax=Axes3D(plt.figure()) # система координат
X, Y = np.meshgrid(np.linspace(-1,1), np.linspace(-1,1)); Z=f([X,Y])
ax.plot_wireframe(X, Y, Z) # каркасна поверхня
ax.scatter(ret['x'][0], ret['x'][1], ret['fun'], c='k') # мінімум
ax.set_xlabel('X0'),ax.set_ylabel('X1'),ax.set_zlabel('Y');plt.show()
"""
Рисунок - Графік функції
"""
