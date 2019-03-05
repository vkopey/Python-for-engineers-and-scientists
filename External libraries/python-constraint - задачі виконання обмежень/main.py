# -*- coding: utf-8 -*-
"""
# python-constraint - задачі виконання обмежень
python-constraint 1.3.1 (http://pypi.org/project/python-constraint) - модуль для розв'язування задач виконання обмежень, ціллю яких є знаходження значень змінних, які відповідають заданим обмеженням. Щоб сформулювати таку задачу потрібно визначити змінні, множину їх значень і обмеження. Модуль може бути використаний для програмування в обмеженнях, яке є видом декларативного програмування. В модулі доступні такі види обмежень: FunctionConstraint, AllDifferentConstraint, AllEqualConstraint, ExactSumConstraint, MaxSumConstraint, MinSumConstraint, InSetConstraint, NotInSetConstraint, SomeInSetConstraint, SomeNotInSetConstraint.
"""
from constraint import *
problem = Problem() # створити задачу
problem.addVariable('a', [1,2,3]) # додати змінну і множину її значень
problem.addVariable('b', [1,2,4])
print problem.getSolutions() # розв'язати задачу (обмежень немає)
# додати обмеження (розкоментуйте потрібні):
problem.addConstraint(lambda a,b: a+b>3, ('a', 'b')) # a+b>3
#problem.addConstraint(AllDifferentConstraint()) # a і b різні
#problem.addConstraint(AllEqualConstraint()) # a і b однакові
#problem.addConstraint(InSetConstraint([2,3])) # a і b в множині {2,3}
print problem.getSolutions() # розв'язати задачу - знайти значення a і b, які відповідають обмеженням
"""
    [{'a': 3, 'b': 4}, {'a': 3, 'b': 2}, {'a': 3, 'b': 1}, {'a': 2, 'b': 4}, {'a': 2, 'b': 2}, {'a': 2, 'b': 1}, {'a': 1, 'b': 4}, {'a': 1, 'b': 2}, {'a': 1, 'b': 1}]
    [{'a': 3, 'b': 4}, {'a': 3, 'b': 2}, {'a': 3, 'b': 1}, {'a': 2, 'b': 4}, {'a': 2, 'b': 2}, {'a': 1, 'b': 4}]
"""
