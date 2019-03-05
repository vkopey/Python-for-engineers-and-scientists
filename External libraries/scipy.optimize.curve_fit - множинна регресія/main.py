# -*- coding: utf-8 -*-
"""
# scipy.optimize.curve_fit - множинна регресія
Функція `scipy.optimize.curve_fit` може бути використана для апроксимації даних функцією багатьох змінних.

Таблиця - Експериментальні дані - залежність *y* від *x0* і *x1*

  x0=|0 1 2
 ----|-----
 x1=0|0 1 2
 x1=1|1 2 3
 x1=2|2 3 7
 
"""

import numpy as np
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score

def f(x, a, b, c): # модель - функція двох змінних x[0] і x[1]
    return a + b*x[0] + c*x[1]

# експериментальні дані:
x = np.array([[0,1,2,0,1,2,0,1,2,],[0,0,0,1,1,1,2,2,2]]) # x0,x1
y = np.array([0,1,2,1,2,3,2,3,7]) # y
#y = np.array([0,1,2,1,2,3,2,3,4]) # спробуйте також
popt, pcov = curve_fit(f, x, y) # апроксимувати нелінійним МНК
print popt # знайдені значення параметрів a, b, c

# рисуємо тривимірні графіки
from mpl_toolkits.mplot3d import axes3d # для рисування 3D графіків
import matplotlib.pyplot as plt
fig = plt.figure() # створити фігуру
ax = fig.add_subplot(111, projection='3d') # додати 3D графік
# змінити форму масивів:
# x0,x1=np.meshgrid(np.array([0,1,2]),np.array([0,1,2]))
# або так:
x0=x[0].reshape((3,3)) # [[0 1 2],[0 1 2],[0 1 2]]
x1=x[1].reshape((3,3)) # [[0 0 0],[1 1 1],[2 2 2]]
y=y.reshape((3,3)) # [[0 1 2],[1 2 3],[2 3 7]]
print "R2=", r2_score(y, f((x0,x1),*popt)) # коефіцієнт детермінації (R-квадрат)
ax.scatter(x0, x1, y) # показати емпіричні точки
xx0, xx1 = np.meshgrid(np.linspace(0, 2, 10), np.linspace(0, 2, 10))
yy=f((xx0,xx1),*popt) # апроксимовані значення
ax.plot_wireframe(xx0, xx1, yy, rstride=1, cstride=1) # показати поверхню
#ax.plot_surface(xx0, xx1, yy, rstride=1, cstride=1) # або
ax.set_xlabel('x0');ax.set_ylabel('x1');ax.set_zlabel('y');plt.show()
"""
Рисунок - Множинна регресія
"""
