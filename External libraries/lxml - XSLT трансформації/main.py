# -*- coding: utf-8 -*-
"""
# lxml - XSLT трансформації
XSLT (eXtensible Stylesheet Language Transformations) - це мова перетворення XML-документів. В прикладі за допомогою lxml до початкового документа XML застосовується таблиця стилів XSLT і отримується перетворений документ XML. Правила вибору даних з початкового документу створюються мовою запитів XPath. 
"""
from lxml import etree
from StringIO import StringIO
xslt_root = etree.XML('''\
 <xsl:stylesheet version="1.0"
     xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
     <xsl:template match="/">
         <foo><xsl:value-of select="/a/b/text()" /></foo>
     </xsl:template>
 </xsl:stylesheet>''') # таблиця стилів XSLT
transform = etree.XSLT(xslt_root) # функція трансформації
f = StringIO('<a><b>Text</b></a>') # документ для трансформації
doc = etree.parse(f) # парсинг документа
print transform(doc) # трансформований документ
