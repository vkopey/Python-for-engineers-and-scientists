# -*- coding: utf-8 -*-
"""
# PyOpenGL - прив'язка до OpenGL
OpenGL - це незалежний від мови програмування і платформи API для рендерингу 2D і 3D векторної графіки. Найчастіше використовується з графічним процесором в програмах для візуалізації, САПР, іграх. PyOpenGL 3.1.0 (http://pyopengl.sourceforge.net) - це прив'язка Python до OpenGL v1.1-4.4, яка створена за допомогою ctypes. Підтримує багато GUI-бібліотек та пов'язаних з OpenGL бібліотек (GLES, GLU, EGL, WGL, GLX, FreeGLUT, GLE). FreeGLUT (http://freeglut.sourceforge.net) - це бібліотека, яка призначена для таких системних задач, як створення вікон, ініціалізація контексту OpenGL і обробка подій. Для роботи програми знадобиться freeglut 3.0.0 MSVC Package (http://www.transmissionzero.co.uk/software/freeglut-devel). Для вивчення PyOpenGL може бути використана офіційна документація (http://www.opengl.org/sdk/docs/man2) та (http://freeglut.sourceforge.net/docs/api.php). Існує також інша прив'язка до OpenGL, яка є частиною pyglet.
"""
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
T=[0,0,0] # вектор переміщень
R=[0,0,1,0] # вектор повороту
def display(  ): # функція відображення OpenGL - рисує об'єкти
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # очистити буфери кольору і глибини
    glColor3f(0, 0, 0) # установити колір RGB (чорний)
    glMatrixMode(GL_MODELVIEW) # режим матриці вигляду
    glLoadIdentity() # одинична матриця
    glTranslatef(T[0], T[1], T[2]) # множить поточну матрицю на матрицю переміщення
    glRotatef(R[0], R[1], R[2], R[3]) # множить поточну матрицю на матрицю повороту навколо вектора
  
    # створює кольорові трикутники   
    glBegin(GL_TRIANGLE_STRIP) # розмежовує вершини примітива (дозволено GL_POINTS, GL_LINES, GL_LINE_STRIP, GL_LINE_LOOP, GL_TRIANGLES, GL_TRIANGLE_STRIP, GL_TRIANGLE_FAN, GL_QUADS, GL_QUAD_STRIP, GL_POLYGON)
    glVertex3f(0.5, 0.5, 0.5) # перша вершина трикутника
    glColor3f(0.9, 0.9, 0.9) # колір наступних вершин
    glVertex3f(-0.5, -0.5, 0) # друга вершина
    glColor3f(0.1, 0.1, 0.1) # колір наступних вершин
    glVertex3f(0.5, -0.5, 0) # третя вершина
    glVertex3f(0.5, 0.5, -0.5) # вершина другого трикутника
    glEnd() # завершити список вершин примітива
    
    glPointSize(3) # розмір точки
    glBegin(GL_POINTS) # точка
    glVertex3f(0,0,0)
    glEnd() 
    
    glBegin(GL_LINES) # рисуємо 3 лінії - осі координат X,Y,Z
    p1=0,0,0
    # для кожного кольору і другої точки лінії
    for c,p2 in [[(1, 0, 0),(1, 0, 0)],[(0, 1, 0),(0, 1, 0)],[(0, 0, 1),(0, 0, 1)]]:
        glColor3f(*c)
        glVertex3f(*p1)
        glVertex3f(*p2)
    glEnd() # завершити рисування
    
    glutWireCube(1) # нарисувати куб
    
    glLineWidth(2) # ширина ліній
    glPushMatrix() # запам'ятати глобальну систему координат
    glTranslatef(0, 0.5, 0) # перемістити систему координат вздовж Y
    glRotatef(45, 0, 0, 1) # повернути в новій системі координат навколо осі Z
    # спробуйте поміняти дві попередні команди місцями
    glutWireCube(0.5) # нарисувати куб
    glPopMatrix() # відновити глобальну систему координат
    
    glTranslatef(0, -0.5, 0) # перемістити систему координат вздовж Y
    # спробуйте закоментувати попередні команди glPushMatrix і glPopMatrix
    glutWireCube(0.25) # нарисувати куб
       
    #glFlush() # виконати GL команди
    glutSwapBuffers() # переключити буфери в режимі подвійної буферизації 

def specialKeyPressed(key, x, y): # переміщує або повертає, якщо натиснуті спеціальні клавіші
    global T,R
    if key == GLUT_KEY_LEFT: T[0] -= 0.1
    elif key == GLUT_KEY_RIGHT: T[0] += 0.1
    elif key == GLUT_KEY_DOWN: T[1] -= 0.1
    elif key == GLUT_KEY_UP: T[1] += 0.1
    elif key == GLUT_KEY_PAGE_DOWN: R[0] += 5
    elif key == GLUT_KEY_PAGE_UP: R[0] += -5
    glutPostRedisplay() 
    
glutInit() # функція ініціалізації glut
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB) # режим відображення
glutInitWindowSize(250, 250) # розмір вікна
glutInitWindowPosition(100, 100) # позиція вікна
glutCreateWindow("My PyOpenGL Demo") # створити вікно
glutSpecialFunc(specialKeyPressed) 
glClearColor(255, 255, 255, 0) # визначає RGBA колір, який буде використовувати glClear
glShadeModel(GL_SMOOTH) # модель затінення GL_FLAT або GL_SMOOTH 

# параметри матеріалів і освітлення (розкоментуйте щоб задіяти)
'''
glMaterialfv(GL_FRONT, GL_AMBIENT, [0.2, 0.2, 0.2, 1.0])
glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.8, 0.8, 0.8, 1.0])
glMaterialfv(GL_FRONT, GL_SPECULAR, [1.0, 0.0, 1.0, 1.0])
glMaterialfv(GL_FRONT, GL_SHININESS, 50.0)
glLightfv(GL_LIGHT0, GL_AMBIENT, [0.0, 1.0, 0.0, 1.0])
glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])
glLightfv(GL_LIGHT0, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
glLightfv(GL_LIGHT0, GL_POSITION, [1.0, 1.0, 1.0, 0.0]);   
glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0.2, 0.2, 0.2, 1.0])
glEnable(GL_LIGHTING)
glEnable(GL_LIGHT0)
glDepthFunc(GL_LESS)
'''
glEnable(GL_DEPTH_TEST) # активізувати перевірку глибини (не показувати невидимі поверхні)

glutDisplayFunc(display) # вказати функцію відображення
glutMainLoop() # головний цикл програми
"""
![](fig.png)

Рисунок - Вікно програми
"""
