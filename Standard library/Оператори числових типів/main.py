# -*- coding: utf-8 -*-
"""
# Оператори числових типів
Приклад показує використання найбільш уживаних операторів для числових типів. В складних виразах дотримуйтесь пріоритету операторів. Наприклад у виразі `1+x*2` спочатку виконується множення, а потім додавання. В наступному списку пріоритет операторів зменшується зверху вниз:

    , [...] {...} `...` - створення кортежу, списку, словника, конвертація рядка
    s[i] s[i:j] s.attr f(...) - індексування, зрізи, атрибути, виклик функції
    +x -x ~x - унарні оператори
    x**y - степінь
    x*y x/y x%y - множення, ділення, остача від ділення
    x+y x-y - додавання, віднімання
    x<<y x>>y - побітовий зсув
    x&y - побітове І
    x^y - побітове XOR (виключне АБО)
    x|y - побітове АБО
    x<y x<=y x>y x>=y x==y x!=y x<>y - порівняння
    x is y   x is not y - ідентичність
    x in s   x not in s - членство
    not x - булеве заперечення
    x and y - булеве І
    x or y - булеве АБО
    lambda args: expr - безіменна функція
"""
a=int("7") # перетворення в ціле
b=long(9.7) # перетворення в довге ціле
x=float("3.14") # перетворення в дійсне
cn1=complex(1,1) # перетворення в комплексне
cn2=(1+2j)/cn1 # ділення комплексних чисел
m=abs(cn2) # модуль комплексного числа
i=bool(2>1) # перетворення в булеве
y=abs(-1.2) #модуль y=(-1.2).__abs__()
print a,b,x,cn2,cn2.real,cn2.imag,m,i,y
z=(-x*y+1)/y**2 # вираз з операторами: унарний мінус, множення, додавання, ділення, степінь
r=9/5 # ділення цілих r=(9).__div__(5)
u=9//5 # цілочисельне ділення
v=9%5 # остача від ділення
w=divmod(9,5) # кортеж 9//5, 9%5
j=2>1 and 1<=0 and not(1==1 or 1!=0 or False) # логічний вираз
k=round(2.91754,2) # заокруглити до 2 знаків після коми
# вивести допомогу по функції: help(round)
print z,r,u,v,w,j,k
print eval("a+b") # значення динамічно побудованого виразу
exec r"print a+b" # виконти Python-код (див. також execfile)