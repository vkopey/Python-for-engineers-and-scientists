# encoding: utf-8
"""
# scipy - похідна і первісна функції
В прикладі дано функцію $y=x^2+4x$. Шляхом чисельного диференціювання знаходиться її похідна $\dot{y}=dy/dx=2x+4$. Шляхом кумулятивного інтегрування знаходиться первісна $Y=\int ydx=x^3/3+2x^2+const$ (http://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.cumtrapz.html#scipy.integrate.cumtrapz). Похідна і первісна можуть бути використані для пошуку екстремумів функції та для розв’язування рівнянь.  Для пошуку екстремуму *y* потрібно розв'язати рівняння $dy/dx=0$. А для пошуку кореня потрібно шукати екстремум первісної *Y*.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumtrapz

X=np.linspace(-5,3)
Y=X**2+4*X # функція
plt.plot(X,Y,'k-')

Y1=np.diff(Y)/np.diff(X) # похідна
plt.plot(X[:-1],Y1,'k--')
Y1=np.gradient(Y,X[1]-X[0]) # або
plt.plot(X,Y1,'k--')

Y_int=cumtrapz(Y, X, initial=0) # первісна
plt.plot(X,Y_int,'k:')
plt.xlabel('$x$');plt.ylabel('$y, \dot{y}, Y$');plt.grid();plt.show()
"""
Рисунок - Функція $y=x^2+4x$ (-), її похідна (--) і первісна (..)
"""
