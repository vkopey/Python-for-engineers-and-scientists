# -*- coding: utf-8 -*-
"""
# Bottle - легкий WSGI веб-фреймворк
Bottle (http://bottlepy.org) - це швидкий, простий і легкий WSGI мікро веб-фреймворк для Python. Він розповсюджується як один файловий модуль і не має ніяких залежностей крім стандартної бібліотеки Python. Містить вбудований сервер і підтримує інші високопродуктивні WSGI сервери. В прикладі використано стару версію Bottle 0.5.8, яка працює навіть на PythonCE. Для тестування прикладу запустіть модуль і введіть в адресному рядку браузера один з URL, наведених нижче.
"""
from bottle import route, run, request, send_file, WSGIRefServer

# декоратор route() пов'язує функцію hello_world з URL-адресами
@route('/') # http://localhost:8080/
@route('/index.html') # http://localhost:8080/index.html
def hello_world():
    return '<h2>Hello World!</h2>' # повертає html відповідь сервера

# тут :name означає будь-який текст.  Також можна використовувати регулярні вирази
@route('/hello/:name') # http://localhost:8080/hello/John
def hello_url(name):
    return 'Hello %s!' % name

# отримання GET параметра
@route('/hello') # http://localhost:8080/hello?name=John
def hello_get():
    name = request.GET['name'] # отримати параметр name
    return 'Hello %s!' % name

# html-форма 
@route('/form') # http://localhost:8080/form
def form():
    return """<form action="/edit" method="post">
User: <input type="text" name="user">
Password: <input type="password" name="password">
<p>Text<Br><textarea name="text">John</textarea></p>
<input type="submit" value="Submit" /></form>"""

# відповідь після натиску кнопки submit на формі
@route('/edit', method='POST')
def hello_post():
    user = request.POST['user'] # значення поля user
    password = request.POST['password'] # значення поля password
    users={'admin':'111'} # словник з парами користувач:пароль
    if user in users and password==users[user]: # якщо користувач і пароль коректні
        text = request.POST['text'] # значення поля text
        return 'Hello %s!' % text
    else:
        return "Login failed" # помилка входу
    
# відсилання статичних файлів (html, jpg, png та ін.)
@route('/:filename#.*#') # http://localhost:8080/static.html http://localhost:8080/pic.png
def static_file(filename):
    send_file(filename, root='') # root - шлях до статичних файлів

run(server=WSGIRefServer, host='localhost', port=8080) # стартувати http сервер