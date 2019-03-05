#-*- coding: utf-8 -*-
"""
# pygments - підсвітка синтаксису в Tkinter
Приклад показує способи підсвітки синтаксису в текстовому віджеті `Tkinter.Text` за допомогою пакету `pygments`.
"""
from Tkinter import *
from pygments.lexers import PythonLexer # лексичний аналізатор Python
from pygments.formatters import RawTokenFormatter
# RawTokenFormatter - для форматування у "сирому" вигляді: тип токена<TAB>repr(рядок токена)\n

root = Tk() # головне вікно
text = Text(root, font=('arial', 10, 'normal')) # віджет для відображення тексту
text.pack() # розташувати
code = u'print "hello" # коментар' # рядок Python коду 
text.insert("end", code) # вставити текст в текстовий віджет

# конфігурувати теги текстового віджету
text.tag_configure("Token.Keyword", foreground='blue', font=('arial', 10, 'bold'))
text.tag_configure("Token.Text", foreground='black', font=('arial', 10, 'normal'))
text.tag_configure("Token.Literal.String", foreground='red', font=('arial', 10, 'normal'))
text.tag_configure("Token.Comment", foreground='darkgreen', font=('arial', 10, 'normal'))

code = text.get("1.0", "end-1c") # отримати текст з текстового віджету
text.delete("1.0", "end") # видалити весь текст з текстового віджету

# перший спосіб:
from pygments import highlight # повертає відформатований текст
for line in highlight(code, PythonLexer(), RawTokenFormatter()).split("\n"): # для кожного рядка тексту, відформатованого за допомогою PythonLexer() та RawTokenFormatter()
    pair=line.split("\t") # розділити рядок символом табуляції
    if pair!=['']: # якщо пара не пуста
        (token, s) = pair
        print token, eval(s) # вивести на консоль
        text.insert("end", eval(s), token) # вставити текст з тегом в віджет

# другий спосіб:
#from pygments import lex # лексичний аналізатор, повертає ітератор токенів
#for token, content in lex(code, PythonLexer()):
#    print token, content
#    text.insert("end", content, str(token))
      
root.mainloop() # головний цикл програми
"""
![](fig.png)

Рисунок - Вікно програми
"""
