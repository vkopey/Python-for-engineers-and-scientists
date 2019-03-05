# encoding: utf-8
"""
# SymPy - символьна математика
SymPy (http://www.sympy.org) - це бібліотека для символьної математики, яка призначена для роботи з математичними виразами в аналітичній (символьній) формі на відміну від чисельних обчислень в SciPy. Її можна розглядати як вільну альтернативу системам символьної математики Maple, Mathcad, Mathematica. Для прикладу SymPy дозволяє інтегрувати, диференціювати, спрощувати вирази, розв'язувати рівняння в символьній формі. 
"""
from sympy import *
x,y,lamda=symbols('x y lamda') # визначити змінні
expr=x+y # вираз
expr2=expr+x # вираз
print expr2.subs(y,2) # вираз шляхом підстановки y=2
print srepr(expr2) # низькорівневе представлення виразу
print expr2.args # кортеж усіх складових виразу
print expr2.atoms() # атоми виразу
print expr2.atoms(Symbol) # атоми (типу Symbol) виразу
print expr2.subs([(x,5),(y,2)]).evalf() # підставити у вираз і обчислити
#print expr2.subs({x:5, y:2}).evalf() # або так
#print expr2.evalf(subs={x:5, y:2}) # або так
#print N(expr2, subs={x:5, y:2}) # або так
print sympify("x**2-1/2") # перетворити рядок у вираз SymPy
expr3=sin(x) # вираз
f=lambdify(x, expr3,"math") # функція для швидкого розрахунку числових значень. Третім аргументом може бути "math" або "numpy" або, наприклад, {"sin":mysin}
print f(0.1) # числове значення

expr4=Integral(sqrt(1/x), x) # вираз-інтеграл
pprint(expr4, use_unicode=False) # виведення в Unicode (True) або ASCII (False). Для Unicode використовуйте для виведення IPython QTConsole або IPython notebook
print latex(expr4) # вивести як LaTeX
from sympy.printing.mathml import *
print mathml(expr4) # вивести як MathML

print simplify(sin(x)**2 + cos(x)**2) # спростити вираз
print expand((x + 1)**2) # розширити поліноміальний вираз

print diff(x**2, x) # похідна
print diff(x**2, x,x) # похідна другого порядку
#print diff(x**2, x,2) # або так
print expr3.diff(x) # похідна
expr5=Derivative(x**2,x) # нерозрахована похідна
init_printing(use_unicode=False) # не використовувати Unicode для виведення
pprint(expr5) # вивести вираз в математичному вигляді
print expr5.doit() # розрахувати похідну
print diff(exp(x*y),x,x,y,y) # мішана похідна
print integrate(sin(x),x) # невизначений інтеграл
print integrate(exp(-x), (x, 0, oo)) # визначений інтеграл
print integrate(exp(-x**2 - y**2), (x, -oo, oo), (y, -oo, oo))
print limit(sin(x)/x, x, 0) # границя
print series(sin(x), x, 0, 8) # ряд функції

print solve(Eq(x**2, 4), x) # розв'язати рівняння
#print solve(x**2-4, x) # або так
# розв'язку не знайдено, якщо solve повертає [] або викликає NotImplementedError
print solve([x-y, x+y], [x, y], dict=True) # розв'язати систему рівнянь
#plot((x-2)**2-2) # нарисувати графік функції
z= Symbol('z', real=True, positive=True) # визначити змінну
print solve([z>2,(z-2)**2-2], z) # розв'язати систему

f=symbols('f', cls=Function) # визначити функцію
diffeq = Eq(f(x).diff(x, x) - 2*f(x).diff(x) + f(x), 0) # диференціальне рівняння
print dsolve(diffeq, f(x)) # розв'язати диференціальне рівняння
