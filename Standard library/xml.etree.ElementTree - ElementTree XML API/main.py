# -*- coding: utf-8 -*-
"""
# xml.etree.ElementTree - ElementTree XML API
Модуль містить визначення типу Element - гнучкого контейнера, який призначений для зберігання ієрархічних структур даних в пам'яті. Використовується для роботи з XML і іншими деревовидними даними. Кожен елемент має такі властивості як тег, набір атрибутів, тестовий рядок, хвостовий рядок, дочірні елементи.
"""
import xml.etree.ElementTree as ET
#ET.VERSION # версія бібліотеки
root = ET.Element("root") # створити кореневий елемент
#root = ET.XML("<root></root>") # або створити з тексту
print ET.tostring(root) # текст елемента ("<root></root>")
print root.tag # тег елемента
root.append(ET.Element("one")) # додати піделемент з таким тегом
two=ET.SubElement(root, "two") # або так
two.attrib["first"] = "1" # створити атрибут елемента
two.text = "text" # текст в елементі
two_one=ET.SubElement(two, "two_one") # додати піделемент
two_one.tail="text" # текст після елемента
root.insert(0, ET.Element("zero")) # вставити елемент в позицію
root.remove(root.find("zero")) # знайти перший піделемент з таким тегом і видалити його
es=root.findall("one") # знайти всі піделементи з таким тегом
es=root.findall(".//one") # знайти за шаблоном:
#'tag' - відповідає елементам верхнього рівня з тегом tag
#'parent/tag' - відповідає елементам з тегом tag, якщо вони дочірні для parent
#'*' - будь-які дочірні елементи
#'.' - починає пошук з поточного вузла
#'//' - відповідає всім вкладеним елементам на всіх рівнях нижче рівня вказаного елемента
txt=root.findtext("two") # знайти текст першого піделемента з таким тегом
print len(root) # кількість піделементів
print root[1].tag # тег другого елемента
print root[1].attrib  # атрибути другого елемента (словник)
nodes = root[:] # усі піделементи або root.getchildren()
for node in root: # цикл по піделементам
    print node.tag

print ET.tostring(root) # вивести як XML

tree = ET.ElementTree(root) # дерево елементів
tree.write("page.xml") # зберегти у файл

tree2 = ET.ElementTree() # або відразу ET.ElementTree("page.xml")
tree2.parse("page.xml") # читати з файлу
subel=tree2.getroot()[0] # перший піделемент
subtree=ET.ElementTree(subel) # піддерево

for parent in tree2.getiterator(): # показати все дерево
    #або getiterator("tagname") - для заданих тегів
    print parent.tag,
#    for child in parent:
#        print ' '*5+child.tag
