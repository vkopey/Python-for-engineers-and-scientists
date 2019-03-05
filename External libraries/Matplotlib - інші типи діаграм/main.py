# -*- coding: utf-8 -*-
"""
# Matplotlib - інші типи діаграм
В прикладі показано створення діаграм розсіювання, гістограм,  контурних діаграм та тривимірних графіків. Інші приклади використання Matplotlib для створення діаграм різного типу можна подивитись тут (http://matplotlib.org/gallery/index.html#).
"""
import numpy as np
import matplotlib.pyplot as plt

# діаграма розсіювання
x=[0, 1, 2, 1] # координати точок
y=[0, 1, 4, 5]
colors=[0.1, 0.4, 0.7, 0.8] # колір точок
sizes=[20,40,60,80] # розміри точок
plt.scatter(x, y, c=colors, s=sizes, alpha=0.7)
plt.xlabel('x');plt.ylabel('y');plt.grid();plt.show()
print "Рисунок - Діаграма розсіювання"

# гістограми
x1=np.random.normal(0, 1.0, 100) # випадкова величина
x2=np.random.normal(2, 1.0, 100) # випадкова величина
plt.figure()
plt.hist(x1, alpha=0.5, bins=7) # гістограма
plt.hist(x2, alpha=0.5, bins=7) # гістограма
plt.xlabel('x');plt.ylabel('y');plt.grid();plt.show()
print "Рисунок - Гістограми"

# контурна діаграма для даних X, Y, Z
X, Y = np.meshgrid(np.linspace(0, 9), np.linspace(0, 9))
Z = X**2+Y**2
plt.figure()
plt.contour(X, Y, Z, 5, colors='white') # без заповнення
plt.contourf(X, Y, Z, 5, cmap=plt.cm.gray) # з заповненням
# або відображення зображень
#plt.imshow(Z, extent=[0, 9, 0, 9], origin='lower', cmap=plt.cm.gray)
#plt.axis(aspect='image') # пропорції осей
plt.colorbar() # смуга зі значеннями Z
plt.xlabel('x');plt.ylabel('y');plt.show()
print "Рисунок - Контурна діаграма"

# тривимірні графіки
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure() # рисунок
ax = Axes3D(fig) # система координат
ax.scatter3D([0,10],[0,10],[0,200], s=200) # точки
ax.plot3D([10,0],[0,10],[0,200], 'ko:') # лінії
#ax.plot_wireframe(X, Y, Z) # каркасна поверхня
ax.plot_surface(X, Y, Z) # поверхня
ax.set_xlabel('x');ax.set_ylabel('y');ax.set_zlabel('z');plt.show()
print "Рисунок - Тривимірний графік"
