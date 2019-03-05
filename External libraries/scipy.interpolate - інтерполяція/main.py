# -*- coding: utf-8 -*-
"""
# scipy.interpolate - інтерполяція
Інтерполяція - це спосіб знаходження проміжних значень величини за її відомим дискретним набором значень. Для інтерполяції і апроксимації сплайнами застосовують функції з модуля `scipy.interpolate` (`interp1d`, `UnivariateSpline`, `interp2d`, `SmoothBivariateSpline` та інші). Сплайн - це функція, область визначення якої розбита на частини, на кожній з яких функція є певним поліномом.
"""
import numpy as np
from scipy.interpolate import interp1d, UnivariateSpline, interp2d
f=lambda x: x**x # функція
x = np.arange(4)
y = f(x)
print x,y # дискретний набір значень
y1 = interp1d(x, y, kind='linear') # лінійна інтерполяція
y2 = interp1d(x, y, kind='quadratic') # інтерполяція квадратичним сплайном
y2 = UnivariateSpline(x, y, k=2, s=0) # або (s - коеф. згладжування)
kn=y2.get_knots() # вузли сплайна
print y1(2.5), y2(2.5), f(2.5) # інтерпольовані і дійсне значення в точці x=2.5

import matplotlib.pyplot as plt
x=np.linspace(0,x.max(),100)
plt.plot(x,f(x),'k-',x,y1(x),'k--',x,y2(x),'k:') # графіки
plt.scatter(kn,y2(kn)) # вузли кв. сплайна 
plt.xlabel('x'),plt.ylabel('y'),plt.grid(),plt.show()
print "Рисунок – Функція (-) та її лінійна (--) і квадратична (..) інтерполяції сплайнами"

f=lambda x,y: x**2+y**2 # функція двох змінних
x=np.array([0,1,2])
y=np.array([0,1,2])
xx, yy = np.meshgrid(x,y) # сітка
z=f(xx,yy) # значення функції у вузлах сітки
z1 = interp2d(x, y, z, kind='linear') # двовимірна лінійна інтерполяція даних x,y,z
print z1(0.5,0.5), f(0.5,0.5)  # інтерпольоване і дійсне значення в точці 0.5, 0.5