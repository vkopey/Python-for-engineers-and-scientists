# -*- coding: utf-8 -*-
"""
# FreeCAD - вільна САПР з Python API
FreeCAD 0.17 (http://www.freecadweb.org) - це вільна параметрична 3D САПР, яка базується на геометричному ядрі Open CASCADE Technology 7.2.0 і володіє Python API. Геометричні моделі створюються способом граничного подання BREP за допомогою її Python-модуля Part, який є прямим зв'язком з OCCT. Повністю OCCT доступна з PythonOCC, але використання FreeCAD модуля Part набагато зручніше. Для виконання прикладу введіть в консолі:

    "e:\FreeCAD 0.17x64\bin\python.exe" main.py
Для виконання з довільного інтерпретатора Python27x64 введіть в консолі:

    c:\Python27\python.exe main.py
"""
import sys
FREECADPATH = r"e:\FreeCAD 0.17x64\bin"
sys.path.append(FREECADPATH) # шлях до бібліотек FreeCAD

import math
import FreeCAD as App # модуль для роботи з програмою
import FreeCADGui as Gui # модуль для роботи з GUI
import Part # workbench-модуль для створення і керування BRep об'єктами

v1=App.Vector(0,0,0) # вектор (або точка)
v2=App.Vector(0,10,0)
v3=App.Vector(5,5,0)
l1=Part.LineSegment(v1,v2) # лінія
e1=l1.toShape() # ребро
# або e1=Part.makeLine((0,0,0),(0,10,0)) # ребро
a1=Part.Arc(v1,v3,v2) # дуга за трьома точками
e2=a1.toShape() # ребро
# або e2=Part.makeCircle(5,App.Vector(0,5,0),App.Vector(0,0,1),-90,90)

bs=Part.BSplineCurve() # B-сплайн
bs.interpolate([(0,0,0),(0,1,1),(0,-1,2)]) # шляхом інтерполяції
# або
#bs.approximate([(0,0,0),(0,1,1),(0,-1,2)]) # шляхом апроксимації
#bs.buildFromPoles([(0,0,0),(0,1,1),(0,-1,2)]) # за списком полюсів
e3=bs.toShape() # ребро

w1=Part.Wire([e1,e2]) # цикл (сукупність ребер)
f1=Part.Face(w1) # грань
trsf=App.Matrix() # матриця трансформації
trsf.rotateZ(math.pi/4) # повернути навколо осі z
trsf.move(App.Vector(5,0,0)) # перемістити
f2=f1.copy() # копія форми
f2.transformShape(trsf) # виконати трансформацію
# або
# f2.rotate(App.Vector(0,0,0),App.Vector(0,0,1),180.0/4)
# f2.translate(App.Vector(5,0,0))
s1=f2.extrude(App.Vector(0,0,10)) # тіло шляхом видавлювання
s2=Part.Wire([e3]).makePipe(f1) # тіло шляхом видавлювання по траєкторії
# або s2=Part.Wire([e3]).makePipeShell([w1],True,True)
s3=f1.revolve(v1,App.Vector(0,1,0),90) # тіло шляхом обертання
s2=s2.fuse(s3) # об'єднання тіл (див. також common, cut, oldFuse)
s2=s2.removeSplitter() # видалити непотрібні ребра (refine shape)
# див. також makeBox, makeCylinder, makeLoft, makeThickness, ...
s1=s1.makeFillet(1,[s1.Edges[1]]) # скруглення (див. також makeChamfer)

print s1.ShapeType # тип форми
print s1.Volume # об'єм (див. також Length, Area, CenterOfMass)
print s1.distToShape(s2)[0] # мінімальна відстань до іншої форми
print s1.Faces[0] # перша грань
print s1.Edges[0] # перше ребро
print type(s1.Edges[0].Curve) # тип кривої першого ребра
print s1.Vertexes[0].Point.x # координата x точки першої вершини

#s1.exportBrep("my.brep") # експорт у форматі BREP (див. також exportStep, exportIges)
#s1 = Part.Shape()
#s1.read("my.brep") # імпорт у форматі BREP

# Наступні команди потрібні тільки для візуалізації створених форм
Gui.showMainWindow() # показати головне вікно
doc=App.newDocument() # створити новий документ
for shape in [l1.toShape(), a1.toShape(), w1, f1, f2, s1, bs.toShape(), s2]:
    Part.show(shape) # показати форму
doc.recompute() # перебудувати
Gui.exec_loop() # головний цикл програми
"""
    Compound
    389.596349447
    0.0
    <Face object at 0000000003AF38D0>
    <Edge object at 0000000003AF4350>
    <type 'Part.Line'>
    -1.27414669346
![](fig.png)

Рисунок - Результати виконання програми
"""
