# -*- coding: utf-8 -*-
"""
# pythonOCC - прив'язка до геометричного ядра Open CASCADE Technology
Open CASCADE Technology (OCCT) - вільна бібліотека мовою С++ для геометричного моделювання (геометричне ядро), яка найчастіше використовується для створення САПР. Геометричні моделі створюються способом граничного подання BREP (boundary representation) у вигляді топологічних форм (вершин, ребер, циклів, граней, поверхонь, твердотільних форм і їх поєднань). pythonOCC 0.18.1 (http://www.pythonocc.org) - бібліотека Python, що дозволяє використання класів OCCT. Побудована за допомогою SWIG - інструмента для пов’язування коду С++ та Python.
"""
from math import pi
from OCC.gp import * # геометричний процесор gp - незбережувані базові геометричні об'єкти
#from OCC.Geom import * # збережувані базові 3D геометричні об'єкти
from OCC.GC import * # алгоритми для побудови елементарних геометричних об'єктів OCC.Geom
from OCC.BRepBuilderAPI import * # класи для моделювання і побудови чисто типологічних структур даних

p1=gp_Pnt(1, 0, 0) # точка (gp_Pnt)
p2=gp_Pnt(1, 2, 0) # точка
p3=gp_Pnt(2, 1, 0) # точка
edge1=BRepBuilderAPI_MakeEdge(p1,p2).Edge() # ребро (TopoDS_Edge)
arc=GC_MakeArcOfCircle(p1,p3,p2).Value() # дуга (Handle_Geom_TrimmedCurve)
edge2=BRepBuilderAPI_MakeEdge(arc).Edge() # створює ребро з дуги

mw=BRepBuilderAPI_MakeWire() # створює контур (BRepBuilderAPI_MakeWire)
mw.Add(edge1) # додати ребро
mw.Add(edge2) # додати ребро
wire=mw.Wire() # контур (TopoDS_Wire)

face=BRepBuilderAPI_MakeFace(wire).Face() # грань (TopoDS_Face)
vector=gp_Vec(p1, gp_Pnt(1, 0, 1)) # вектор (gp_Vec)
from OCC.BRepPrimAPI import * # забезпечує API для створення примітивів (призм, тіл обертання, витягувань, сфер, циліндрів ...)
solid1 = BRepPrimAPI_MakePrism(face, vector).Shape() # призма (TopoDS_Shape)

axis=gp_Ax1(gp_Pnt(),gp_Dir(0,1,0)) # вісь Y (gp_Ax1)
solid2 = BRepPrimAPI_MakeRevol(face, axis, pi).Shape() # тіло обертання (TopoDS_Shape)

from OCC.BRepAlgoAPI import * # забезпечує новий API для булевих операцій з формами (об'єднань, вирізів, перетинів)
solid3=BRepAlgoAPI_Fuse(solid2, solid1).Shape() # тіло після об'єднання (TopoDS_Shape); деколи важлива послідовність аргументів

from OCC.Display.SimpleGui import init_display # засоби для створення GUI
display, start_display, add_menu, add_function_to_menu = init_display()
display.set_bg_gradient_color(255,255,255,255,255,255) # колір фону
display.DisplayShape(solid3) # показати форму
display.FitAll()                            
start_display()
"""
![](fig.png)

Рисунок - Результати виконання програми
"""
