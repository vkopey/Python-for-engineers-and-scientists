# -*- coding: utf-8 -*-
"""
# scipy.stats.kde - ядрова оцінка густини розподілу
Ядрова оцінка густини розподілу - це непараметричний метод оцінки функції густини випадкової величини за вибіркою (http://en.wikipedia.org/wiki/Kernel_density_estimation). Задається формулою

$$f(x) = \frac{1}{nh} \sum_{i=1}^n K\left(\frac{x-x_i}{h}\right),$$

де $x_i$ - значення незалежних і однаково-розподілених випадкових величин; *h* - параметр згладжування; *K* - статистичне ядро - симетрична, але не обов'язково додатна функція з інтегралом рівним одиниці. В прикладі використовується Гаусове ядро:

$$K(u)=\frac{1}{\sqrt{2\pi}}e^{-0.5u^2}.$$
"""
import numpy as np
from scipy.stats import kde
import matplotlib.pyplot as plt
x1 = np.random.normal(0, 3, 50) # вибірка з нормального розподілу розміром 50, m=0, std=3
x2 = np.random.normal(4, 1, 50) # вибірка з нормального розподілу розміром 50, m=4, std=1
x = np.concatenate([x1,x2]) # об'єднати дані 
density = kde.gaussian_kde(x, bw_method=None) # функція щільності. Можна також визначити свій метод згладжування bw_method. Може бути багатовимірна.
xgrid = np.linspace(x.min(), x.max(), 100)
plt.hist(x, bins=8, normed=True, color='y') # гістограма
plt.plot(xgrid, density(xgrid), 'k-') # функція щільності
plt.xlabel('x');plt.ylabel('y');plt.grid();plt.show()
"""
Рисунок - Ядрова оцінка густини розподілу
"""
