#-*- coding: utf-8 -*-
"""
# pygments - підсвітка синтаксису
Підсвітка синтаксису - це виділення синтаксичних конструкцій тексту за допомогою різних шрифтів, їх кольорів і написань. Використовується для спрощення сприйняття тексту. Підсвітка синтаксису виконується за допомогою лексичного аналізатора, який визначає окремі лексеми (послідовність символів, що має певне значення). Пакет `pygments` 2.2.0 (http://pygments.org) призначений для підсвічування синтаксису, підтримує близько 300 мов, дозволяє створювати нові лексичні аналізатори, виводить в багатьох форматах (HTML, RTF, LaTeX та ін.), може використовуватись в командному рядку або як бібліотека.
"""
from pygments import highlight # повертає відформатований текст
from pygments.lexers import PythonLexer # лексичний аналізатор Python
from pygments.formatters import HtmlFormatter # для форматування у вигляді HTML
code = u'print "Hello World" # коментар' # Юнікод (!) рядок Python коду
print highlight(code, PythonLexer(), HtmlFormatter()) # повертає проаналізований  PythonLexer() та відформатований HtmlFormatter() текст
#print HtmlFormatter().get_style_defs('.highlight') # повертає текст стилю CSS

# все в одному файлі HTML
#print highlight(code, PythonLexer(), HtmlFormatter(full=True))

# все в одному файлі HTML окрім стилю. Стиль окремим файлом python.css
#print highlight(code, PythonLexer(), HtmlFormatter(full=True,cssfile='python.css'))

# новий лексичний аналізатор на основі регулярних виразів
from pygments.lexer import RegexLexer
from pygments.token import *
class MyLexer(RegexLexer):
    tokens = {'root': [(r'[^#]+', Text),(r'#.*\n', Comment),(r'\n.*', Text)]} # послідовність (рег. вираз, токен)
print highlight(code, MyLexer(), HtmlFormatter())