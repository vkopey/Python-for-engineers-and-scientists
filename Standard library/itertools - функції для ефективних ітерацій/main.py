# -*- coding: utf-8 -*-
"""
# itertools - функції для ефективних ітерацій
Модуль itertools містить функції, які створюють ітератори і призначені для ефективних ітерацій по даним. Для економії пам’яті ітератори застосовуються з оператором `for`, але в прикладі вони передані функції `list`. Це зроблено тільки для зменшення об’єму коду прикладу. 
"""
from operator import add # бінарний оператор +
from itertools import *
print list(izip('ab', 'cd')) # зшиває перший з першим, другий з другим  і т.д.
# count - послідовні значення, cycle - повторює послідовність нескінченно
for n,i in izip(count(), cycle('abc')):
    if n>5: break
    print (n,i),
print
print list(chain('ab','cd')) # об'єднує в один
print list(compress('abcd', [1,0,1,0])) # тільки ті елементи, яким відповідає 1
print list(dropwhile(lambda x: x!='c', 'abcd')) # відкидати поки True
print list(takewhile(lambda x: x!='c', 'abcd')) # приймати поки True
print [(k,list(g)) for k, g in groupby('aaabbac')] # групує
print list(ifilter(lambda x: x in 'bd', 'abcd')) # фільтрує
print list(imap(add, (1,2,3), (4,5,6))) # add(1,4), add(2,5), ...
#print list(imap(lambda x,y: x+y, (1,2,3), (4,5,6))) # або
print list(starmap(add, [(1,2), (4,5)])) # add(1,2), add(4,5), ...
print [list(i) for i in tee('abc',3)] # створює 3 незалежні ітератори
print "Комбінаторні генератори:"
print list(product('ab','cd')) # декартів добуток
print list(product('ab',repeat=2)) # декартів добуток з собою
#print list(product('ab','ab')) # або
print list(permutations('abc',2)) # усі можливі перестановки з двох елементів
print list(combinations('abc',2)) # усі можливі комбінації з двох елементів
print list(combinations_with_replacement('abc',2)) # тут дозволені повтори
