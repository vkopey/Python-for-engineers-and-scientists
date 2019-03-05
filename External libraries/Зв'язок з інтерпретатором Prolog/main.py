# -*- coding: utf-8 -*-
"""
# Зв'язок з інтерпретатором Prolog
В прикладі показано спосіб взаємодії Python програми з інтерпретатором Prolog (SWI-Prolog) за допомогою `subprocess.Popen`. Більш тісний зв'язок з SWI-Prolog реалізує пакет PySwip (http://github.com/yuce/pyswip).
"""
from subprocess import Popen, PIPE, STDOUT
with open('family.pl', 'w') as f: # створити Prolog-програму
    f.write('isParent("Ivan","Petro"). isChild(X,Y) :- isParent(Y,X).')
p = Popen(r'"c:\Program Files (x86)\swipl\bin\swipl.exe" -q family.pl', shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
print p.communicate('isChild(X,"Ivan").') # надіслати запит і отримати результат
"""
    ('\r\nX = "Petro".\r\n\r\n\r\n', None)
"""
