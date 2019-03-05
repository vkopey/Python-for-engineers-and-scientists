# -*- coding: utf-8 -*-
"""
# ttk.Treeview - дерево елементів
Модуль `ttk` містить класи, які дозволяють використання віджетів `Tk` з підтримкою тем оформлення. Клас `ttk.Treeview` дозволяє відображати ієрархічну колекцію (дерево) елементів. Кожний елемент може мати текстовий надпис, рисунок і список значень даних.
"""
import Tkinter, ttk 
def btn1Click(event):
    '''Обробник події відпускання кнопки 1 миші'''
    tree = event.widget # віджет, що викликав подію
    node = tree.focus() # вибраний елемент дерева (його id)
    print node # id
    print tree.item(node) # словник опцій вузла:
    #{'text':'', 'image':'', 'values':'', 'open':0, 'tags':''}
    print tree.item(node,'text') # текст вибраного елемента
    # або print tree.item(node)['text']
    print tree.parent(node) # предок
    print tree.index(node) # індекс елемента в списку споріднених
    print tree.prev(node) # попередній споріднений
    print tree.next(node) # наступний споріднений
    print tree.get_children(node) # список дочірніх
    print tree.set(node) # словник зі значеннями колонок
    print tree.exists(node) # чи існує елемент?
def dbl_btn1Click(event):
    '''обробник події подвійного натиску кнопки 1 миші'''
    print 'dblClicked'
def btn3Click(event):
    '''обробник події натиску кнопки 3 миші'''
    print 'btn3Clicked'
def tagClicked(event):
    '''Обробник подій натиску мишею на тезі'''
    print 'tagClicked'
def treeOpenClose(event):
    '''Обробник подій відкриття і закриття піддерева'''
    print 'opened/closed'
def treeSelect(event):
    '''Обробник події вибору елемента'''
    print 'selected'
        
root = Tkinter.Tk() # створити головне вікно
img = Tkinter.PhotoImage(file='folder.gif') # рисунок
sbar_y = ttk.Scrollbar(orient="vertical") # створити вертикальну смугу прокручування
sbar_x = ttk.Scrollbar(orient="horizontal") # створити горизонтальну смугу прокручування
tree = ttk.Treeview(height=10) # створити дерево
tree['selectmode']=Tkinter.EXTENDED # дозволити вибір багатьох елементів
# або так:
tree.config(selectmode=Tkinter.NONE) # заборонити вибір елементів
#tree.state(('disabled',)) # заблокувати tree
tree['columns'] = ('state',) # додати колонки
tree.column('state', width=100, anchor='center') # параметри колонки 'state'
tree['displaycolumns']='state' # показувати колонку
tree.heading('#0', text='Item',image=img) # надпис на колонці 0
tree.heading('state', text='State') # надпис на колонці 'state'
sbar_y['command'] = tree.yview # під час прокручування змінювати положення дерева
sbar_x['command'] = tree.xview
tree['yscrollcommand'] = sbar_y.set # значення повзунка смуги прокручування
tree['xscrollcommand'] = sbar_x.set

# розмістити віджети
sbar_y.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)
sbar_x.pack(side=Tkinter.BOTTOM, fill=Tkinter.X)
tree.pack(side=Tkinter.LEFT, fill=Tkinter.Y)

# прив'язки до обробників подій
tree.bind('<ButtonRelease-1>', btn1Click)
tree.bind('<Double-Button-1>', dbl_btn1Click)
tree.bind('<Button-3>', btn3Click)
tree.bind('<<TreeviewSelect>>', treeSelect) # обробник події вибору
tree.bind('<<TreeviewOpen>>', treeOpenClose) # обробник події відкриття піддерева
tree.bind('<<TreeviewClose>>', treeOpenClose) # обробник події закриття піддерева

tree.insert('', 0, 'first', text='item 1', image=img) # додати перший елемент 'first' після кореневого ''
tree.item('first', text='item 1!',open=1) # змінити опції елемента 'first'
tree.set('first', 'state', '***') # значення для 'first' в колонці 'state'
id=tree.insert('', 'end', text='item 2') # додати другий елемент після ''
id=tree.insert(id, 'end', text='item 21',tags=('tag1',)) # додати дочірні до id
tree.tag_configure('tag1', foreground='blue') # колір тегу
tree.tag_bind('tag1', '<3>', tagClicked); # вказати обробник події натиску на праву кнопку миші
tree.insert('first', 'end', 'child', text='Child') # додати дочірній 'child' до 'first' в кінець
tree.insert('child', 'end', text='Child') # додати дочірній до 'child'
tree.insert('first', 'end', text='Child',values=('***',)) # додати дочірній до 'first'
tree.move('child', '', 'end') # перемістити 'child' разом з дочірніми в кінець кореня        
# або
#tree.detach('child') # відділити від дерева (зі збереженням в пам'яті)
#tree.reattach('child', '', 'end') # знову прикріпити до дерева (предок '', позиція 'end') 
#tree.delete('child') # повністю видалити
#tree.set_children('child',id,'first') # замінює дитину елемента 'child' новими дітьми (id,'first')
tree.focus('first') # установити фокус на перший елемент
tree.selection_set(('first',)) # вибрати елементи
print tree.selection() # вибрані елементи
tree.see('first') # прокрутити дерево до елемента, щоб він став у полі зору

root.mainloop()# головний цикл обробки подій
"""
![](fig.png)

Рисунок - Дерево елементів
"""
