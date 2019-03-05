# -*- coding: utf-8 -*-
"""
# OMPython -  інтерфейс OpenModelica Python
Modelica - це основана на рівняннях об'єктно-орієнтована мова для зручного моделювання складних фізичних систем, які містять, наприклад, механічні, електричні, гідравлічні, термічні субкомпоненти. OpenModelica 1.12 (http://www.openmodelica.org/) - це вільне середовище симуляції мовою Modelica. OMPython - це інтерфейс з OpenModelica мовою Python, який забезпечує доступ до OpenModelica API. Для його інсталяції введіть в консолі:

    cd e:\OpenModelica\share\omc\scripts\PythonInterface
    c:\Python27\python.exe -m pip install .
В прикладі розв'язується просте диференціальне рівняння з початковою умовою $x(0)=1$:

$\frac{dx}{dt} = ax$.

"""
code='''model Simple
    Real x(start=1);
    parameter Real a=1;
equation
    der(x)=a*x;
end Simple;''' # модель мовою Modelica 
with open('Simple.mo', 'w') as f: f.write(code) # створити файл моделі
import os, sys
sys.path.insert(0, r"e:\OpenModelica\share\omc\scripts\PythonInterface") # шлях до модулів
from OMPython import OMCSession, ModelicaSystem

# перший спосіб - використання OMCSession:
omc = OMCSession()
omc.sendExpression('loadFile("Simple.mo")')
omc.sendExpression('setParameterValue(Simple, a, 2)')
omc.sendExpression('simulate(Simple)')
omc.sendExpression('plot(x)')
print omc.sendExpression('val(x , 1.0)') # результат x(time=1.0)

# або більш зручний спосіб:
mod=ModelicaSystem("Simple.mo","Simple")
print mod.getParameters()
mod.setParameters(a=2)
mod.setSimulationOptions(stopTime=2.0)
mod.simulate()
print mod.getSolutions('time','x') # результати як масиви

# або компілювати модель і симулювати без OMPython:
omc.sendExpression('buildModel(Simple)') # компілювати
os.environ["PATH"] += os.pathsep + r"e:\OpenModelica\bin" # шлях до dll
param='''outputFormat=csv
stopTime=2
a={}
''' # значення параметрів
for i,p in enumerate([1, 2, 3]): # для кожного значення
    with open('override%d.txt'%i, 'w') as f: f.write(param.format(p)) # створити файл зі значеннями параметрів
    os.system(r'Simple.exe -overrideFile=override%d.txt -r=Simple_%d.csv'%(i,i)) # симуляція
"""
    7.38908993012
    {'a': 1.0}
    (array([0., 0.002, 0.004, ..., 1.998, 2., 2.]), array([1., 1.00400801, 1.0080321, ..., 54.38076352, 54.59872293, 54.59872293]))

![](fig.png)

Рисунок - Результати симуляції
"""
