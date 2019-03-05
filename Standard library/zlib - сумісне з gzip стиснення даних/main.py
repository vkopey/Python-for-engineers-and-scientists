# -*- coding: utf-8 -*-
"""
# zlib - сумісне з gzip стиснення даних
Модуль zlib містить функції для стиснення та декомпресії даних з використанням бібліотеки zlib.
"""
import zlib
s="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
c=zlib.compress(s, 9) # стиснути дані з найвищим рівнем
#c=s.encode('zlib') # або так
s=zlib.decompress(c) # виконати декомпрессію
#s=c.decode('zlib') # або так
print len(s),len(c) # довжина даних до і після стиснення
