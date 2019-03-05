# -*- coding: utf-8 -*-
"""
# pyglet - кросплатформна віконна і мультимедійна бібліотека
pyglet 1.3.2 (http://bitbucket.org/pyglet/pyglet) - це віконна і мультимедійна бібліотека, яка призначена для розробки ігор та інших візуально багатих програм. Підтримує обробку вікон, обробку подій GUI, графіку OpenGL, завантаження зображень і відео, а також відтворення звуків и музики. Працює на Windows, OS X і Linux. В прикладі показано простий переглядач 3D об'єктів OpenGL на основі pyglet.
"""
import pyglet
from pyglet.window import Window, mouse
from pyglet.gl import *

class MyWindow(Window): # клас вікна
    def __init__(self, *args, **kwargs):
        super(MyWindow,self).__init__(*args, **kwargs)
        self.x,self.y = 0,0 # кути повороту
        self.label = pyglet.text.Label(x=20,y=20,color=(0, 0, 0, 255)) # надпис
        glClearColor(1, 1, 1, 1) # визначає RGBA колір, який буде використовувати glClear
        glEnable(GL_DEPTH_TEST) # активізувати перевірку глибини (не показувати невидимі поверхні)
        
    def on_resize(self, width, height): # під час зміни розміру вікна
        aspectRatio = width/height # відношення сторін
        glViewport(0, 0, width, height) # установлення порту виведення
        glMatrixMode(GL_PROJECTION) # режим матриці проекцій
        glLoadIdentity() # одинична матриця
        gluPerspective(35.0, aspectRatio, 1.0, 1000.0) # матриця перспективної проекції
        glMatrixMode(GL_MODELVIEW) # режим матриці вигляду
        glLoadIdentity()

    def on_draw(self): # під час необхідності перерисування
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) # очистити буфери кольору і глибини
        glMatrixMode(GL_MODELVIEW) # режим матриці вигляду
        glPushMatrix() # запам'ятати глобальну систему координат
        glTranslatef(0, 0, -600) # перемістити систему координат вздовж Z
        self.label.text='ax=%d ay=%d'%(self.x,self.y) # змінити надпис
        self.label.draw() # нарисувати надпис
        glRotatef(self.x, 1, 0, 0) # повернути в новій системі координат навколо осі X
        glRotatef(self.y, 0, 1, 0) # повернути в новій системі координат навколо осі Y
        self.drawAxes() # нарисувати осі
        self.drawObject() # нарисувати об'єкт
        glPopMatrix() # відновити глобальну систему координат
        
    def drawAxes(self): # рисує осі X,Y,Z
        glBegin(GL_LINES) # розмежовує вершини примітива (лінії)
        for r,g,b,x,y,z in [(1,0,0,1000,0,0), (0,1,0,0,1000,0), (0,0,1,0,0,1000)]:
            glColor3f(r, g, b) # колір наступної вершини
            glVertex3f(-x, -y, -z) # перша вершина
            glVertex3f(x, y, z) # друга вершина
        glEnd() # завершити список вершин примітива

    def drawObject(self): # рисує об'єкт
        glBegin(GL_TRIANGLES) # розмежовує вершини примітива (трикутника)
        glColor3f(0, 0, 1) # колір наступної вершини
        glVertex3f(0, 0, 0) # перша вершина
        glVertex3f(100, 0, 0) # друга вершина
        glVertex3f(100, 100, 0) # третя вершина
        glEnd() # завершити список вершин примітива
    
    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers): # під час руху миші
        if buttons & mouse.LEFT:
            self.x-=dy # змінити кут повороту на величину переміщення миші 
            self.y+=dx
        
MyWindow(width=400, height=400, caption="pyglet",resizable=True) # вікно
pyglet.app.run() # цикл обробки подій
"""
![](fig.png)

Рисунок - Вікно програми
"""
