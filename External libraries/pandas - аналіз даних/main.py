# -*- coding: utf-8 -*-
"""
# pandas - аналіз даних
pandas (http://pandas.pydata.org) - бібліотека, яка базується на NumPy і містить високопродуктивні та зручні у використанні структури даних та інструменти обробки і аналізу даних. За функціональністю pandas подібна на табличний процесор Excel. Основними структурами даних є `Series` (одновимірний масив ndarray з мітками осі) та `DataFrame` (таблиця з мітками осей (рядків і стовпців)). Приклад описує основні можливості pandas 0.20.3.
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
_='\n'
x1 = [0, 2, 2, 3, 9]
x2 = [12, 12, None, 20, 31]
dataSet = zip(x1,x2) # підготувати дані
df = pd.DataFrame(data = dataSet, columns=['X1', 'X2']) # об'єкт DataFrame
sr = pd.Series([1,3,np.nan,7,9]) # об'єкт Series
print df,_ # вивести таблицю
#print df.head() # вивести початок таблиці
#df.to_csv('rodStats.csv',index=False,header=False) # зберегти у файл csv
#df = pd.read_csv('rodStats.csv',names=['X1', 'X2']) # прочитати з файлу csv

print df.dtypes,_ # типи даних колонок
print df.X1,_ # вміст колонки (Series)
#df['X1'] # або
print df['X1'].unique(),_ # унікальні значення колонки
df[0:2] # перші 2 рядка (DataFrame)
print df.loc[:,'X1'],_ # індексування (Series містить тільки X1)
#df[['X1']] # або (DataFrame містить тільки X1)
print df[df['X1'] == 0],_ # умовне індексування (DataFrame)
# або:
df[(df['X1'] == 0) & (df['X2'] > 0)] # | - or, & - and, ~ - not 
df['X2'][df['X1'] == 0] # (Series)

print df['X1'].values,_ # конвертація в numpy.ndarray
df.dropna() # відкинути рядки з відсутніми даними (None) (див. також fillna)
df.sort_index(axis=1) # сортувати за колонками (1) або рядками (0) 
df.sort_values(['X1'], ascending=False) # сортувати за X1 (за спаданням)
df['X3'] = np.sqrt(df['X1']**2+df['X2']**2) # додати нову колонку
print df['X3'].map(lambda x: x+1),_ # застосувати функцію для кожного елемента Series (див. також apply і applymap для DataFrame)
print df.groupby(df['X1']).mean(),_ # групувати за X1 і знайти середнє в групах
print df.pivot(index='X1', columns='X2', values='X3'),_ # звідна таблиця, де X1 - рядки, X2 - колонки, X3 - значення (див. також pd.pivot_table)
print df.stack(),_ # ієрархічне представлення даних (див. також unstack, MultiIndex - ієрархічний індекс)
print pd.crosstab(df['X1'], df['X2']),_ # таблиця частот факторів X1,X2

print df.describe(),_ # статистика для кожної колонки (див. також mean, std, ...)
print df.cov(),_ # коваріація (математичне сподівання добутків відхилень випадкових величин)
print df.corr() # кореляція (коеф. корел. Пірсона = covXY/(Sx*Sy))

#df.plot(kind='bar') # візуалізація
#df.plot(x='X1', y='X2')
#plt.show()
