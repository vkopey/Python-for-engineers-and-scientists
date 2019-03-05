# -*- coding: utf-8 -*-
"""
# decimal - дійсні числа довільної точності
На відміну від типу даних `float`, модуль `decimal` дозволяє точно подавати дробові десяткові значення.
"""
import sys
import decimal # модуль для арифметики довільної точності
print 0.1*7==0.7 # False
print decimal.Decimal('0.1')*7 == decimal.Decimal('0.7') # True
print sys.float_info # інформація про тип float
x=1.7976931348623157e+308 # найбільше float
print 2*x # результат: inf
x=decimal.Decimal('1.7976931348623157e+308') # дійсне довільної точності
print x.as_tuple() # кортеж у вигляді (знак, мантиса, порядок)
print 2*x # результат: 3.5953862697246314E+308
