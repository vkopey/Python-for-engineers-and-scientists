# -*- coding: utf-8 -*-
"""
# lxml - простий і швидкий парсинг XML і HTML
lxml 4.1.0 (http://lxml.de) - це Python-бібліотека для обробки XML і HTML, яка є прив'язкою до C бібліотек libxml2 і libxslt. Володіє повною підтримкою XML, є швидкою і зручною у використанні, сумісна з ElementTree API. В прикладі розглядається використання HTMLParser та xpath для отримання ключових слів некоректного HTML документу з тегу meta. XPath (XML Path Language) - це мова запитів до елементів XML документа.
"""
from StringIO import StringIO
from lxml import etree
broken_html=r"""<html><head>
<meta content="Python, XML" name="keywords" />
<head>""" # некоректний документ HTML
parser=etree.HTMLParser()
tree=etree.parse(StringIO(broken_html), parser) # парсинг
root=tree.getroot() # кореневий елемент (html)
es=root.findall('head/meta') # знайти усі теги meta
for e in es:
    if 'name' in e.attrib and 'content' in e.attrib: # якщо є такі атрибути
        if e.attrib['name']=="keywords":
            print e.attrib['content']

# або за допомогою мови запитів xpath:
es=tree.xpath("head/meta[@name='keywords']/@content")
es=tree.xpath("child::head/child::meta[attribute::name='keywords']/attribute::content") # або повний синтаксис xpath
print es[0]
