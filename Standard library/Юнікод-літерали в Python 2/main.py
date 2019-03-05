#-*- coding: utf-8 -*-
"""
# Юнікод-літерали в Python 2
В Python 2 використовувати юнікод-літерали без застосування символу `u` можна так:
"""
from __future__ import unicode_literals
print type('текст') # <type 'unicode'>, а не <type 'str'>
print type(u'текст') # <type 'unicode'>
