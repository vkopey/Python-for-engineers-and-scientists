# -*- coding: utf-8 -*-
"""
# CGI-програма `simple.py` - генерація форми запиту
CGI (Common Gateway Interface) - стандартний протокол для взаємодії програми веб-сервера із зовнішньою консольною програмою (CGI-програмою або шлюзом). Після запиту клієнта CGI-програма виконується сервером в окремому процесі, обробляє дані запиту і генерує відповідь сервера. Будь-яка CGI-програма повертає в стандартний потік виведення заголовок HTTP, пустий рядок і дані. Запустіть сервер та в адресному рядку браузера введіть:

    http://localhost/cgi/simple.py

Для тестування методу GET справте нижче `method="post"` на `method="get"`.
"""
html="""<html><body>
<form action="/cgi/get_post.py" method="post">
First Name: <input type="text" name="first_name"><br />
Last Name: <input type="text" name="last_name" />
<input type="submit" value="Submit" /></form>
</body></html>"""
print "Content-type: text/html\r" # заголовок
print "\r" # пустий рядок
print html # дані
"""
![](fig1.png)

Рисунок - Результати роботи CGI-програми simple.py
"""
