# -*- coding: utf-8 -*-
"""
# PyParsing - зручний синтаксичний аналіз
Синтаксичний аналіз (парсинг) - це процес зіставлення послідовності лексем (неподільних груп символів) певної мови з її формальною граматикою (способом опису мови). Лексеми отримуються шляхом лексичного аналізу (токенізації). PyPasing 2.2.0 (http://pypi.org/project/pyparsing) - модуль для синтаксичного аналізу, який реалізує альтернативний і більш зручний підхід для створення і використання граматик, у порівнянні з традиційним lex/yacc або використанням регулярних виразів. Модуль містить класи для створення граматик прямо в Python-коді.
"""
from __future__ import print_function
from pyparsing import *
s="hello world!" # текст, який будемо парсити
# вираз для парсингу:
word=Word(alphas) # слово з букв, alphas='abcde...'+'ABCDE...'
print(type(word))
#<class 'pyparsing.Word'>
p="hello"+word+Literal("!")
# або p=And([Literal("hello"), word, Literal("!")])
print(type(p))
#<class 'pyparsing.And'>
try: # тут бажане перехоплення помилки
    print(p.parseString(s)) # знайти p в s ОДИН раз
#['hello', 'world', '!']
    print(p.parseString(s).asList()[0])
#hello
except: pass

for x in Word(alphas).searchString(s): # знайти УСІ слова в s
    print(x)
#['hello']
#['world']
    
print(ZeroOrMore("o").searchString(s)) # 0 або більше
#[['o'], [], ['o']]
print(OneOrMore("o").searchString(s)) # 1 або більше
#[['o'], ['o']]
res=[x for x in OneOrMore("o").scanString(s)]
print(res[0]) # кортеж
#((['o'], {}), 4, 5)

p=Literal('hello')^Literal('world') # або 'hello' або 'world'
# або p=Or([Literal('hello'), Literal('world')])
print(p.parseString("world"))
#['world']

p=Literal("world")|Literal("hello") # знайти перше world або hello
# або MatchFirst([Literal("world"),Literal("hello")])
print(p.parseString(s))
#['hello']

p=Literal("world")&Literal("hello") # як +, але не послідовно, а в довільному порядку
# або p=Each([Literal("world"), Literal("hello")])
print(p.parseString(s))
#['hello', 'world']

# літерал і слово (якщо є; але без нього)
p=Literal('hello')+Optional(Suppress(Word(alphas)))
print(p.parseString(s)) # без другого слова
#['hello']

def fn(s, loc, toks):
    print(s, loc, toks)
p=Word(alphas).setParseAction(fn)+Word(alphas) # викликає функцію fn для першого слова
p.parseString(s)
#hello world! 0 ['hello']

p=Word(alphas).setResultsName("word1")+Word(alphas+'!') # у виразі задано ім'я для першого слова
print(p.parseString(s).word1)
#hello

p=Literal("hello").setParseAction(replaceWith("hi"))
print(p.transformString(s)) # заміна hello на hi
#hi world!

alphasUA='АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯабвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
alphasRU='АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
print(Word(alphasUA).parseString("привіт world!")[0])
#привіт

# іменовані регулярні вирази
print(Regex(r"hello (?P<name>.*)").parseString(s).name)
#world!

print(SkipTo(Literal("world")).parseString(s)) # все що до літералу "world"
#['hello ']

p=Combine(Word(alphas)+Literal(" ")+Word(alphas)) # об'єднати
print(p.parseString(s))
#['hello world']

w = Word(nums)
p = Forward() # попередня декларація
p << ('['+OneOrMore(Group(p)^w)+']') # рекурсія
print(p.parseString('[1 2 [3 4]]'))
#['[', '1', '2', ['[', '3', '4', ']'], ']']
