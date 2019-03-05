# -*- coding: utf-8 -*-
"""
# scipy.optimize.root - розв'язування систем рівнянь
Для розв'язування систем нелінійних рівнянь чисельними методами застосовують функцію `scipy.optimize.root`. Її необов'язковий параметр `method` визначає метод розв'язування системи (`hybr`, `lm`, `df-sane`, `broyden1`, `broyden2`, `anderson`, `linearmixing`, `diagbroyden`, `excitingmixing`, `krylov`). За замовчуванням використовується `hybr`. В прикладі розв'язується система:

$$ 2x_0^2 + 2x_1=0; $$
$$ x_0-2=0. $$

"""
from scipy.optimize import root
def f(x, a, b, c): # векторна функція
    return [a*x[0]**2 + b*x[1],
            x[0]-c] # список лівих частин рівнянь
sol = root(f, [0, 0], args=(2,2,2)) # розв'язати систему рівнянь з початковими значеннями коренів x0=[0, 0]
print sol.x # корені
