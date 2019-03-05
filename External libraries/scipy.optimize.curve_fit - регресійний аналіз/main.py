# -*- coding: utf-8 -*-
"""
# scipy.optimize.curve_fit - регресійний аналіз
Регресійний аналіз (http://en.wikipedia.org/wiki/Regression_analysis) - це статистичний метод дослідження впливу однієї або декількох незалежних змінних *x* на залежну змінну *y*. Для пошуку функціональної залежності *f(x)*, яка найкраще описує емпіричну залежність *y* від *x*, застосовують метод найменших квадратів (МНК). МНК оснований на мінімізації суми квадратів відхилень значень функції *f(x)* від значень *y*.
"""
import numpy as np
from scipy.optimize import curve_fit, leastsq
import matplotlib.pyplot as plt # для побудови графіків
x=np.array([0, 1, 2, 3]) # емпіричні значення x
y=np.array([1, 1.5, 3, 4]) # емпіричні значення y

# за допомогою scipy.optimize.curve_fit:
def f(x, a, b): # модель - лінійна залежність y=a*x+b"
    return a*x+b # тут можна змінити модель на іншу функцію
popt, pcov = curve_fit(f, x, y) # апроксимувати дані залежністю f за допомогою нелінійного МНК
print popt # знайдені значення параметрів `a` і `b`
print pcov # коваріаційна матриця для `a` і `b`
print np.sqrt(np.diag(pcov)) # стандартні відхилення для `a` і `b`
residuals = y - f(x,*popt) # відхилення
print "RMSE",(np.sum(residuals**2)/(residuals.size-2))**0.5 # стандартна помилка (root-mean-square error (RMSE)) 
ymean = np.mean(y) # середнє `y`
ss_res = np.dot(residuals, residuals)
ss_tot = np.dot((y-ymean), (y-ymean))
print "R^2:", 1-ss_res/ss_tot # коефіцієнт детермінації (R-квадрат)
print "R^2:", np.corrcoef(y, f(x,*popt))[0,1]**2 # або так

xa=np.linspace(0,3,100) # 100 значень на проміжку 0..3
ya=f(xa, *popt) # масив значень f з параметрами a=popt[0], b=popt[1]
plt.plot(x, y, 'ko--') # нарисувати емпіричну залежність
plt.plot(xa, ya, 'k-') # нарисувати апроксимовану залежність
plt.xlabel('x'); plt.ylabel('y'); plt.show()
print "Рисунок - Лінійна регресія"

# або за допомогою scipy.optimize.leastsq:
def residuals_(p,x,y): # p - кортеж параметрів
    return y - f(x, p[0], p[1]) # повертає відхилення
ans=leastsq(func=residuals_,x0=(1,1),args=(x,y),full_output=True) # мінімізує суму квадратів
print ans[0] # знайдені значення параметрів `a` і `b`

# або за допомогою scipy.stats.linregress (тільки лінійна регресія):
from scipy.stats import linregress
slope, intercept, r_value, p_value, std_err=linregress(x, y)
print slope, intercept # знайдені значення параметрів лінійної залежності
print "R^2:", r_value**2 # коефіцієнт детермінації (R-квадрат)
