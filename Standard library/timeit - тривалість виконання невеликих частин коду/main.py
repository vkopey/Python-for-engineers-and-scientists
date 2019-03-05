#-*- coding: utf-8 -*-
"""
# timeit - тривалість виконання невеликих частин коду 
Модуль `timeit` дозволяє просто визначати тривалість виконання невеликих частин коду. Для великих частин коду використовуйте модуль `time`. З прикладу видно, що `sin(x)` виконується швидше ніж `math.sin(x)`. 
"""
import timeit
print timeit.timeit('math.sin(x)', setup='import math; x = 1', number=1000000) # час  виконання 1000000 раз (cекунд)
print timeit.timeit('sin(x)', setup='from math import sin; x = 1', number=1000000)
