# -*- coding: utf-8 -*-
"""
# pyDatalog - логічне програмування в Python
Логічне програмування основане на виведенні нових фактів з існуючих відповідно правил логічного виведення. pyDatalog 0.17.1 (http://sites.google.com/site/pydatalog) - пакет, який додає парадигму логічного програмуавання в Python. Datalog - повністю декларативна підмножина мови логічного програмування Prolog. В декларативному програмуванні програма описує **що** потрібно досягти, а в імперативному - **як**. Програма мовою Datalog містить факти, правила логічного виведення і запити. Наприклад, фактом є твердження "Іван є батьком Петра", правило логічного виведення - "якщо Y батько X, то X дитина Y", а запит - "знайти усіх дітей Петра". 
"""
from __future__ import unicode_literals
from pyDatalog import pyDatalog
pyDatalog.create_terms("isParent, isChild, isSibling, X, Y, Z, c") # Datalog-терми (змінні з великої букви)
+isParent("Ivan","Petro") # додати факт (isParent - предикат)
+isParent("Ivan","Stepan") # предикати можуть бути кирилицею: globals()['назва']
# правила логічного виведення ("<=" - "якщо, то"):
isChild(X,Y) <= isParent(Y,X) # якщо Y батько X, то X дитина Y
isSibling(X,Y) <= isParent(Z,X) & isParent(Z,Y) & ~(X==Y)
# запити:
print isChild("Petro", X).data # знайти батька Петра
print isChild(X,"Ivan").data # знайти усіх дітей Івана
print isSibling(X,Y).data # знайти усіх братів
(c[X]==len_(Y)) <= (isParent(X,Y))
print (c[X]==Y).data # знайти кількість дітей батька X

pyDatalog.clear() # очистити базу даних
pyDatalog.create_terms("abs, f, g") # abs - вбудована функція
print ((X==[1,2,-3]) & (Y==abs(X[2])+1)).data # знайти X,Y
print (X.in_(range(5)) & Y.in_(range(5)) & (Z==X+Y) & (Z<2)).data # знайти X,Y
f["Ivan"]=2 #  факт (f - предикат)
f["Petro"]=0
#+(f['Petro'] == 0) # або
print ((f[X]==Y) & (Y>0)).data # знайти X,Y
del f["Ivan"] # видалити
(g[X]==3) <= (X=="Ivan") 
print ((g[X]==Y)).data # знайти X,Y
"""
    [(u'Ivan',)]
    [(u'Petro',), (u'Stepan',)]
    [(u'Petro', u'Stepan'), (u'Stepan', u'Petro')]
    [(u'Ivan', 2)]
    [((1, 2, -3), 4)]
    [(0, 1, 1), (1, 0, 1), (0, 0, 0)]
    [(u'Ivan', 2)]
    [(u'Ivan', 3)]
"""
