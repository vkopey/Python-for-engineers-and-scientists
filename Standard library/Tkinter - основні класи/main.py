# -*- coding: utf-8 -*-
"""
# Tkinter - основні класи
В прикладі показано використання основних класів Tkinter для створення програм з графічним інтерфейсом. Використано такі класи як `Tk` (головне вікно), `Frame` (фрейм або прямокутна область на екрані), `Button` (кнопка), `Label` (надпис), `Entry` (текстове поле), `Checkbutton` (прапорець), `Radiobutton` (перемикач), `Listbox` (список), `Canvas` (канва або область для рисування), `Scale` (шкала), `Menu` (меню), `StringVar` (текстова змінна), `IntVar` (ціла змінна), `BooleanVar` (булева змінна), `DoubleVar` (дійсна змінна).
"""
from Tkinter import *
class MyFrame(Frame): # клас, успадкований від Frame
    def __init__(self, master=None): # конструктор
        Frame.__init__(self, master) # виклик конструктора базового класу
        self.grid() # розмістити фрейм
        self.button1 = Button(self, text="Button", command=self.command1) # створити кнопку, встановити її властивості
        # або встановити властивості так:
        self.button1["text"] = "Button" # надпис
        self.button1["command"] =  self.command1 # метод для виконання
        # або встановити властивості так:
        self.button1.config(text="Button",command=self.command1)
        self.button1.grid(row=0, column=0) # розмістити в рядку 0 і стовпчику 0
        self.label1=Label(self,text="Label") # створити надпис
        self.label1.grid(row=0, column=1) # розмістити
        self.tv=StringVar() # створити рядкову змінну
        self.entry1=Entry(self,textvariable=self.tv) # створити текстове поле, пов'язати з змінною tv
        self.entry1.insert(0, 3.14) # вставити текст (або так: self.tv.set("3.14"))
        self.entry1.grid(row=0, column=2) # розмістити
        self.bv=BooleanVar() # створити булеву змінну
        self.check1=Checkbutton(self,variable=self.bv) # створити прапорець, пов'язати зі змінною bv
        self.check1.grid(row=0, column=3) # розмістити
        self.iv=IntVar() # створити цілу змінну
        self.radio1=Radiobutton(self, text='Radio1',variable=self.iv, value=1) # створити перемикач, пов'язати з змінною iv
        self.radio1.grid(row=1, column=0) # розмістити
        self.radio2=Radiobutton(self, text='Radio2',variable=self.iv, value=2) # створити перемикач, пов'язати зі змінною iv
        self.radio2.grid(row=1, column=1) # розмістити
        self.iv.set(2) # установити значення 2 (включити другий перемикач)
        self.list1=Listbox(self) # створити список
        self.list1.grid(row=1, column=2,rowspan=5,columnspan=1) # розмістити
        for x in ["Red","Blue","Green"]: # заповнити список
            self.list1.insert(END,x)
        self.list1.selection_set(0) # вибрати елемент 0
        self.list1.bind("<Double-Button-1>", self.event2) # пов'язати подію з методом
        self.canvas1 = Canvas(root, width=200, height=160, bg='white') # створити канву
        self.line1=self.canvas1.create_line(0,0,100,100, width=5) # створити лінію на канві
        self.canvas1.grid(row=2, column=0) # розмістити
        self.canvas1.bind("<Motion>", self.event1) # пов'язати подію з методом
        self.dv=DoubleVar() # створити дійсну змінну
        self.scale1 = Scale(self, from_=-10.0, to=10.0, resolution=0.5, label='Scale', orient=HORIZONTAL, variable=self.dv) # створити шкалу, пов'язати зі змінною dv
        self.scale1.grid(row=2, column=1) # розмістити
        menu1 = Menu(self) # створити меню
        master.config(menu=menu1) # установити меню для вікна
        menu11 = Menu(menu1) # створити підменю
        menu1.add_cascade(label='Menu', menu=menu11) # додати підменю
        menu11.add_command(label='Exit',command=sys.exit) # додати елемент меню
    def command1(self): # метод command1
        x=float(self.tv.get()) # присвоїти `x` значення tv
        self.tv.set(x**2) # установити tv значення x**2
        print self.bv.get() # вивести значення bv
        print self.iv.get() # вивести значення iv
        print self.dv.get() # вивести значення dv
        print self.list1.get(self.list1.curselection()) # вивести вибраний у списку елемент
    def event1(self,event): # метод event1 (обробник події)
        self.tv.set(event.x) # установити tv значення координати миші `x`
        self.canvas1.coords(self.line1,(event.x, event.y, event.x+50, event.y+50)) # змінити координати лінії line1
    def event2(self,event): # метод event2 (обробник події)
        event.widget["fg"]="red" # змінити значення властивості fg віджета, що викликав подію
        self.command1() # виклик методу command1
root = Tk() # створити головне вікно
app = MyFrame(master=root) # створити наш фрейм на вікні
app.mainloop() # головний цикл обробки подій
root.destroy() # знищити вікно
"""
![](fig.png)

Рисунок - Вікно програми
"""
