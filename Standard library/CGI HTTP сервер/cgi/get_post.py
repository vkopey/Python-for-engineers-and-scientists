# -*- coding: utf-8 -*-
"""
# CGI-програма `get_post.py` - обробка запитів GET і POST
CGI-програма може отримати доступ до рядка запиту (даних форми) за допомогою `cgi.FieldStorage`. Запустіть сервер та в адресному рядку браузера введіть для тестування методів GET і POST, відповідно:

    http://localhost/cgi/get_post.py?first_name=Volodymyr&last_name=Kopey
    http://localhost/cgi/get_post.py`

Або, якщо форма розташована у файлах HTML, відповідно:

    http://localhost/GET.html
    http://localhost/POST.html
"""
import cgi # модуль для обробки cgi 
form = cgi.FieldStorage() # об'єкт FieldStorage
first_name = form.getvalue('first_name') # дані з першого поля
last_name  = form.getvalue('last_name') # дані з другого поля
print "Content-type: text/html\r\n\r\n" # заголовок, пустий рядок
print "<h2>Hello %s %s</h2>" % (first_name, last_name) # дані
"""
![](fig2.png)

Рисунок - Результати роботи CGI-програми get_post.py
"""
