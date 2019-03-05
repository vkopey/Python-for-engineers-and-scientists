# -*- coding: utf-8 -*-
"""
# PyQt4 - створення елемента керування
В прикладі показано створення нового елемента керування (GUI-віджету) `MyButton` шляхом успадкування класу `QPushButton` (кнопка). На відміну від базового класу нова кнопка володіє атрибутом `state`, логічне значення якого змінюється на протилежне під час натиску на неї. Крім того це значення відображається на самій кнопці.
"""
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class MyButton(QPushButton): # клас успадковує QPushButton
    state = True
    def __init__(self, state,parent=None): # конструктор
        super(MyButton, self).__init__(parent) # виклик конструктора QPushButton
        self.state=state # стан кнопки (True, False)
        self.setText(self.state.__str__()) # установити надпис на кнопці
        # приєднати сигнал clicked() до слота self.change_state()
        self.connect(self, SIGNAL("clicked()"), self.change_state)
    def change_state(self): # обробник сигналу clicked()
        if self.state: # якщо стан True
            self.emit(SIGNAL("state_true"), self.state) # генерувати сигнал state_true
            self.state=False # змінити стан
        else: # інакше генерувати сигнал state_false
            self.emit(SIGNAL("state_false"), self.state)
            self.state=True # змінити стан
        self.setText(self.state.__str__()) # установити надпис на кнопці
        
class My_Dialog(QDialog): # клас вікна успадковує QDialog
    def __init__(self, parent=None): # конструктор
        super(My_Dialog, self).__init__(parent) # виклик конструктора QDialog
        self.resize(230, 100) # змінити розмір вікна
        self.pushButton1 = MyButton(True,self) # кнопка
        self.pushButton1.setGeometry(QRect(25, 50, 90, 30)) # змінити геометрію кнопки
        self.pushButton2 = MyButton(False,self) # кнопка
        self.pushButton2.setGeometry(QRect(120, 50, 90, 30)) # змінити геометрію кнопки
        self.lineEdit = QLineEdit(self) # поле редагування
        self.lineEdit.setGeometry(QRect(25, 10, 90, 30)) # змінити геометрію поля редагування
        # приєднати сигнали до слотів
        self.connect(self.lineEdit, SIGNAL("textChanged(QString)"),
                     self, SLOT("setWindowTitle(QString)"))
        self.connect(self.pushButton1, SIGNAL("state_true"), self.slot)
        self.connect(self.pushButton2, SIGNAL("state_true"), self.slot)      
    def slot(self): # обробник сигналу state_true
        button = self.sender() # компонент, що надіслав сигнал
        # якщо це ніякий компонент або не об'єкт класу MyButton
        if button is None or not isinstance(button, MyButton):
            return # то вийти
        global x # звернення до глобальної змінної
        if button==self.pushButton1: x+=1 # якщо кнопка pushButton1
        else: x-=1 # інакше
        self.lineEdit.setText(x.__str__())
x=0 # глобальна змінна        
app = QApplication(sys.argv) # створити застосування
dialog = My_Dialog() # створити вікно
dialog.show() # показати вікно
app.exec_() # виконати застосування
"""
![](fig.png)

Рисунок - Вікно програми
"""
