# -*- coding: utf-8 -*-
"""
# HTMLParser - простий парсер HTML і XHTML 
Цей модуль визначає клас HTMLParser, який служить як основа для синтаксичного аналізу файлів HTML і XHTML. Для парсингу необхідно створити похідний від HTMLParser клас і перевизначити його методи. У Python 2.7 працює також з некоректними html. Для високопродуктивного парсингу використовуйте lxml (з ElementTree API) або Beautiful Soup.
"""
from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser): # успадковує HTMLParser і перевизначає його методи, шукає дані усіх тегів <p>
    def __init__(self): # конструктор
        HTMLParser.__init__(self)
        self.intag = False # в середині тегу?
        self.data = [] # список знайдених даних
    def handle_starttag(self, tag, attrs):
        "Викликається коли знайдено початковий тег (наприклад <p>)"
        print "Початковий тег", tag
        print "Атрибути", attrs
        if tag=='p': # якщо тег p
            self.intag=True # знаходимось всередині тегу 
    def handle_endtag(self, tag):
        "Викликається коли знайдено кінцевий тег (наприклад </p>)"
        print "Кінцевий тег:", tag
        if tag=='p': # якщо тег p
            self.intag=False # знаходимось поза тегом p
    def handle_data(self, data):
        "Викликається коли знайдено дані ... (наприклад <p>...</p>)"
        print "Дані:", data
        if self.intag: # якщо в середині тегу p
            self.data.append(data) # додати в список результатів дані

parser = MyHTMLParser() # об'єкт класу
html="""<html><body>
<p align="justify">Текст</p>
<a href="index.html">Індекс</a>
</body></html>""" # документ HTML для парсингу
parser.feed(html) # виконати парсинг
parser.close()
print "\nЗнайдені дані:", parser.data[0]
#parser.handle_starttag('a', [('href',"index.html")])
