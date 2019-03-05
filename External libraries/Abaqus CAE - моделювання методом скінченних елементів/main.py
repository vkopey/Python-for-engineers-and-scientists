# -*- coding: utf-8 -*-
"""
# Abaqus/CAE - моделювання методом скінченних елементів
Abaqus/CAE 6.14 (http://www.3ds.com/products-services/simulia) - комерційне середовище для розв'язування задач механіки деформівного твердого тіла, гідрогазодинаміки і електродинаміки методом скінченних елементів (МСЕ). Володіє зручним API мовою Python 2.7, який дозволяє створювати прикладні програми. В прикладі створюється осесиметрична модель деталі, яка розтягується осьовим навантаженням. Зазвичай послідовність розв'язування задач МСЕ містить етапи: створення геометрії, властивостей матеріалу, генерація сітки елементів, створення граничних умов, розв'язування рівнянь і аналіз результатів.
"""
from abaqus import *
from abaqusConstants import *
Mdb() # створити нову модель
m=mdb.models['Model-1'] # модель
import os
os.chdir(r"C:\Abaqus") # робочий каталог

s=m.ConstrainedSketch(name='__profile__', sheetSize=200.0) # ескіз
s.ConstructionLine((0.0, -100.0), (0.0, 100.0)) # допоміжна лінія
points=[(10.0, 0.0),(0.0, 0.0),(0.0, 10.0),(10.0, 10.0),(5.0, 5.0), (10.0, 0.0)] # точки ескізу
for p1,p2 in zip(points[:-1],points[1:]):
    s.Line(p1,p2) # лінія за точками
p=m.Part(name='Part-1', dimensionality=AXISYMMETRIC, type=DEFORMABLE_BODY) # деталь
p.BaseShell(sketch=s) # на основі ескізу s

mat=m.Material(name='Material-1') # матеріал
mat.Elastic(table=((2.1e11, 0.3), )) # модуль Юнга і коеф. Пуасона
m.HomogeneousSolidSection(name='Section-1', material='Material-1', thickness=None) # однорідна секція матеріалу
region = p.Set(faces=p.faces, name='Set-1') # геометричний регіон
p.SectionAssignment(region=region, sectionName='Section-1') # зв'язати секцію і деталь

a = m.rootAssembly # збірка
inst=a.Instance(name='Part-1-1', part=p, dependent=ON) # її елемент
a.Set(vertices=inst.vertices.findAt(((5,5,0),)), name='CenterPoint') # точка для результатів 
p.seedPart(size=1.0, deviationFactor=0.1, minSizeFactor=0.1) # розміри сітки
p.generateMesh() # створити сітку

m.StaticStep(name='Step-1', previous='Initial') # статичний крок
region=a.Set(edges=inst.edges.findAt(((1,0,0),)), name='Encastre')
m.EncastreBC(name='BC-1', createStepName='Step-1', region=region, localCsys=None) # гранична умова на нижньому торці
region=a.Surface(side1Edges=inst.edges.findAt(((1,10,0),)), name='Surf-1')
m.Pressure(name='Load-1', createStepName='Step-1', region=region,  magnitude=-10e6) # тиск на верхньому торці

job=mdb.Job(name='Job-1', model='Model-1') # створити задачу
job.submit() # надіслати розв'язувачу
job.waitForCompletion() # чекати завершення

from visualization import * # для візуалізації результатів
odb=openOdb("C:/Abaqus/Job-1.odb") # відкрити базу даних результатів
f=odb.steps['Step-1'].frames[-1].fieldOutputs # результати останнього фрейму
reg=odb.rootAssembly.elementSets['ENCASTRE'] # нижній торець
print f['S'].getSubset(position=INTEGRATION_POINT, region=reg).values[0].mises # еквівалентне напруження в елементі 0 регіону
reg=odb.rootAssembly.nodeSets['CENTERPOINT'] # центральна точка
print f['U'].getSubset(position=NODAL, region=reg).values[0].data # переміщення Ux і Uy (.magnitude - сумарне)
odb.close() # закрити базу даних результатів
"""
    7578833.5
    [ 0.00022752  0.00070781]
![](fig.png)

Рисунок - Еквівалентні напруження за критерієм Мізеса-Губера (Па)
"""
