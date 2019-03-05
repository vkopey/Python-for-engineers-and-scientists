# -*- coding: utf-8 -*-
"""
# PyQt4 - елементи керування QtGui
Більш складний приклад використання таких елементів керування як `QMainWindow` (головне вікно), `QMenuBar` (смуга меню), `QMenu` (меню), `QAction` (дія GUI), `QTextBrowser` (текстовий браузер), `QComboBox` (список), `QDial` (пристрій регулювання), `QCheckBox` (прапорець), `QPixmap` (рисунок), `QLabel` (надпис або рисунок), `QTreeWidget` (дерево), `QTreeWidgetItem` (елемент дерева), `QFileDialog` (вікно вибору файлу), `QMessageBox` (вікно з повідомленням), `QApplication` (GUI-застосування). Програма Qt Designer дозволяє полегшити створення складних GUI в режимі WYSIWYG. Після створення нею файлу опису GUI `main.ui` потрібно згенерувати код Python за допомогою програми `pyuic`:

    pyuic.py -x main.ui -o main.py
"""
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class MyWindow(QMainWindow): # клас вікна успадковує QMainWindow
    def __init__(self, parent=None): # конструктор
        super(MyWindow, self).__init__(parent) # виклик конструктора QMainWindow
        self.resize(400, 300) # змінити розмір вікна
        self.menubar = QMenuBar(self) # створити смугу меню
        self.menubar.setGeometry(QRect(0, 0, 400, 24)) # геометрія
        # підменю:
        self.menuFile = QMenu(self.menubar) # меню File в menubar
        self.menuFile.setTitle("File") # установити надпис
        self.menuNew = QMenu(self.menuFile) # меню New в menuFile
        self.menuNew.setTitle("New")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setTitle("About")
        # дії меню:
        self.actionNewItem = QAction(self)
        self.actionNewItem.setText("New Item")
        self.actionOpen = QAction(self)
        self.actionOpen.setText("Open")
        # додати до меню дії:
        self.menuNew.addAction(self.actionNewItem)
        self.menuFile.addAction(self.menuNew.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        
        self.textBrowser = QTextBrowser(self) # текстовий браузер
        self.textBrowser.setGeometry(QRect(10, 30, 130, 200))
        self.comboBox = QComboBox(self) # комбінований список
        self.comboBox.addItems([str(i) for i in range(1,11)]) # додати елементи
        self.comboBox.setGeometry(QRect(10, 240, 100, 20))
        self.dial = QDial(self) # пристрій регулювання
        self.dial.setNotchesVisible(True) # установити шкалу
        self.dial.setGeometry(QRect(150, 30, 50, 50))
        self.checkBox=QCheckBox("CheckBox",self) # прапорець
        self.checkBox.setTristate(True) # установити три можливі стани
        self.checkBox.setGeometry(QRect(150, 110, 100, 20))
        self.pixmap=QPixmap() # рисунок
        self.pixmap.load(u"pic.png") # завантажити
        self.label=QLabel(self) # надпис
        self.label.setPixmap(self.pixmap) # установити рисунок
        self.label.setGeometry(QRect(150, 150, 100, 100))
        self.treeWidget = QTreeWidget(self) # дерево
        self.treeWidget.setGeometry(QRect(250, 30, 140, 200))
        item_0 = QTreeWidgetItem(self.treeWidget) # додати кореневий елемент
        item_1 = QTreeWidgetItem(item_0) # додати дочірній елемент до item_0
        item_0.setText(0,'editable') # установити текст елемента
        item_1.setText(0,'11')
        item_0.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEditable | Qt.ItemIsDragEnabled | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled) # властивості елемента
        self.treeWidget.expandToDepth(2) # розвернути дерево до рівня 2
        # приєднати сигнали до слотів:        
        self.connect(self.comboBox,SIGNAL("currentIndexChanged(int)"), self.slot2)
        self.connect(self.dial, SIGNAL("valueChanged(int)"), self.slot3)
        self.connect(self.checkBox, SIGNAL("stateChanged(int)"), self.slot4)
        self.connect(self.actionOpen, SIGNAL("triggered()"), self.slot1)
        self.connect(self.actionNewItem, SIGNAL("triggered()"), self.slot2)
        self.connect(self.treeWidget, SIGNAL("itemDoubleClicked(QTreeWidgetItem*,int)"), self.slot4)
    
    #обробники відповідних сигналів:
    def slot1(self):
        filename=QFileDialog.getOpenFileName(self, "MyFile") # ім'я файлу з вікна вибору файлу
        self.textBrowser.append("<font color=blue>" + filename + "</font>") # додати в текстовий браузер
        
    def slot2(self):
        if self.treeWidget.currentItem()!=None: # якщо існує поточний елемент дерева
            item = QTreeWidgetItem(self.treeWidget.currentItem()) # створити дочірній елемент до поточного
            item.setText(0,'New') # його текст
            item.setTextColor(0,QColor(255,0,0)) # його колір
            item.setCheckState(0, Qt.Checked) # установити стан
        else: # інакше вивести вікно повідомлення
            QMessageBox.warning(self, "MessageBox","select parent item!")
        self.textBrowser.append("index {0} - text {1}".format(self.comboBox.currentIndex(), self.comboBox.currentText())) # додати в браузер індекс і текст поточного елемента списку
    
    def slot3(self):
        self.checkBox.setText(self.dial.value().__str__()) # значення пристрою регулювання
    
    def slot4(self):
        if self.treeWidget.currentItem()!=None: # якщо існує поточний елемент дерева
            if self.treeWidget.currentItem().checkState(0): # якщо стан вибраний
                self.treeWidget.removeItemWidget(self.treeWidget.currentItem(),0) # видалити поточний елемент
        self.textBrowser.append("checkBox {0}".format(self.checkBox.checkState())) # додати в браузер стан перемикача
        
app = QApplication(sys.argv) # створити застосування
label = QLabel("<font color=red size=72><b>" + "Hello" + "</b></font>") # надпис (з'являється перед появою головного вікна)
label.setWindowFlags(Qt.SplashScreen) # властивості вікна
label.show() # показати
import time
time.sleep(1) # затримка на 1 с.
label.hide() # сховати надпис
window = MyWindow() # створити вікно
window.show() # показати вікно
#QTimer.singleShot(10000, app.quit) # вийти через 10 с.
app.exec_() # виконати застосування
"""
![](fig.png)

Рисунок - Вікно програми
"""
