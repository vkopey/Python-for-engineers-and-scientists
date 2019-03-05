# -*- coding: utf-8 -*-
"""
# Юнікод-рядки
Юнікод-рядок (unicode) - це послідовність символів Юнікоду. Для створення літерала юнікод-рядка перед лапками потрібно поставити символ `u`. Рядки unicodе і str підтримують однакові операції.
"""
s='звичайний рядок'
us=u'юнікод-рядок'
print type(s),isinstance(s, str) # <type 'str'> True
print type(us),isinstance(us, unicode) # <type 'unicode'> True
s2=us.encode('utf-8') # кодує в звичайний рядок utf-8
us2=s.decode('utf-8') # декодує звичайний рядок utf-8 в юнікод-рядок
us2=unicode(s, 'utf-8') # або так
print type(s2) # <type 'str'>
print type(us2) # <type 'unicode'>
print len('рядок') # 10 , бо кодується utf-8 (символи кодуються 1-6 байтами)
print len(u'рядок') # 5
