# -*- coding: utf-8 -*-
"""
# xml.dom.minidom - мінімальна реалізація DOM
XML - це стандарт побудови мов розмітки (мов, що використовують спеціальні анотації для розмітки тексту) ієрархічно структурованих даних. DOM (Document Object Model) - це незалежний від мови програмування програмний інтерфейс, який дозволяє створювати, читати і змінювати XML документи. DOM подає XML документи як деревовидну структуру, де кожен вузол є об'єктом, що відповідає частині документу. xml.dom.minidom - це мінімальна реалізація інтерфейсу DOM, який подібний на ті, що використовуються в інших мовах. Вона простіша ніж повний DOM і суттєво менша.
"""
from xml.dom import minidom

################# Document Objects (minidom.Document()) ##########

# створити XML документ з кореневим тегом 'html'
doc=minidom.getDOMImplementation().createDocument(None, 'html', None)
html=doc.documentElement # кореневий елемент

# або створити XML документ так:
#doc=minidom.Document() # XML документ
#html=doc.createElement("html")# створити кореневий елемент (тільки один)
#doc.appendChild(html) # додати дочірній вузол (тут doc - вузол)

body = doc.createElement('body') # створити елемент
html.appendChild(body) # додати дочірній вузол до html

div = doc.createElement('div') # створити елемент
txtNode=doc.createTextNode('Text') # створити текстовий вузол
#print txtNode.data # вміст текстового вузла
div.appendChild(txtNode) # додати дочірній вузол до div
body.appendChild(div) # додати дочірній вузол до body

################## Element Objects (minidom.Element()) ###########

elements=doc.getElementsByTagName('div') # знайти усі елементи з тегом div
#print elements[0].toxml() # вивести перший з них в форматі XML
el=div # елемент div
#print el.tagName # ім'я тегу
el.setAttribute('id', '1') # задати атрибути
el.setIdAttribute('id') # задати ID атрибут (для getElementById())
#print el.hasAttribute('id') # чи має атрибут 'id'
#print el.getAttribute('id') # значення атрибута 'id' 
#print el.getAttributeNode('id') # вузол атрибута 
el.removeAttribute('id')
el.setAttribute('id', '1')
el=doc.getElementById('1') # знайти елемент з ID='1'

################# Node Objects (minidom.Node()) ##################

node=div # вузол елемента div
#print node.nodeName # ім'я вузла (div)
#print node.nodeType # тип вузла (1 - ELEMENT_NODE)
#print node.nodeValue # текстове значення вузла
#print node.hasChildNodes() # чи має підвузли
#print node.parentNode # батьківський вузол
#print node.nextSibling # наступний споріднений
#print node.previousSibling # попередній споріднений
#print node.childNodes # дочірні вузли
#print node.firstChild # перший дочірній
#print node.lastChild # останній дочірній
#print node.hasAttributes() # чи має атрибути
#print node.attributes['id'].nodeValue # значення атрибута id
#print node.isSameNode(div) # чи це той самий вузол
clon=node.cloneNode(True) # клонувати з підвузлами
body.insertBefore(clon, div) # вставити дочірній перед div
body.removeChild(clon) # видалити дочірній clon
body.appendChild(clon) # додати дочірній
body.removeChild(clon)

######################## xml.dom.minidom ###########################
print doc.toprettyxml(' ') # вивести в форматі з відступами
f=open("my.html","w") # відкрити файл для запису
f.write(doc.toprettyxml(' ')) # зберегти документ
f.close()

doc2 = minidom.parse('my.html') # читати XML документ з файлу
doc3=minidom.parseString('<A>x</A>') # читати XML документ з рядка
#print doc3.toxml() # вивести документ в форматі XML
"""
    <?xml version="1.0" ?>
    <html>
      <body>
       <div id="1">Text</div>
      </body>
    </html>
"""
