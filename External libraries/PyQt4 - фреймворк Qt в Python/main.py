# -*- coding: utf-8 -*-
"""
# PyQt4 - фреймворк Qt в Python
PyQt4 (http://www.riverbankcomputing.com/software/pyqt) - це "прив'язка" фреймворку Qt до мови Python. Qt - це багатоплатформовий програмний фреймворк для створення ПЗ мовою C++. Містить класи для створення GUI, роботи з мережею, базами даних, OpenGL, мультимедіа і т.д. Існує також прив'язка з більш вільними умовами ліцензування PySide (http://wiki.qt.io/PySide), яка сумісна на рівні API з PyQt. В прикладі показано програму з GUI для розрахунку квадрату числа. Цей приклад буте також працювати в PySide 1.2.4, якщо замінити рядок `PyQt4` на `PySide`.
"""
import sys
from PyQt4.QtCore import * # базові класи
from PyQt4.QtGui import * # GUI класи
class My_Dialog(QDialog): # клас вікна успадковує QDialog
    def __init__(self, parent=None): # конструктор
        super(My_Dialog, self).__init__(parent) # виклик конструктора QDialog
        self.setWindowTitle("x**2") # надпис вікна
        self.resize(150, 100) # змінити розмір вікна
        self.pushButton = QPushButton("Calculate",self) # кнопка
        self.pushButton.setGeometry(QRect(25, 50, 90, 30)) # змінити геометрію кнопки
        self.lineEdit = QLineEdit("2",self) # поле редагування
        self.lineEdit.setGeometry(QRect(25, 10, 90, 30)) # змінити геометрію поля редагування
        self.lineEdit.setFocus() # установити фокус вводу
        # приєднати сигнал clicked() до слота self.slot
        self.connect(self.pushButton, SIGNAL("clicked()"), self.slot)        
    def slot(self): # обробник сигналу clicked()
        x=float(self.lineEdit.text()) # введене у поле число
        self.lineEdit.setText((x**2).__str__()) # вивести у поле
app = QApplication(sys.argv) # створити застосування
dialog = My_Dialog() # створити вікно
dialog.show() # показати вікно
app.exec_() # виконати застосування
"""
![](fig.png)

Рисунок - Вікно програми
"""
