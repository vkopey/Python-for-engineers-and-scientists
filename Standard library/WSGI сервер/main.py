# -*- coding: utf-8 -*-
"""
# WSGI сервер
WSGI (Web Server Gateway Interface) - стандарт взаємодії між Python-програмою і самим веб-сервером. За стандартом WSGI веб-програма повинна бути об'єктом, що викликається, і приймати два параметра: словник змінних середовища (environ) і обробник запиту (start_response). Модуль `wsgiref.simple_server` реалізує простий HTTP-сервер, який виконує одну WSGI-програму. Запустіть сервер та в адресному рядку браузера введіть:

    http://localhost/?name=Volodymyr
    http://localhost
"""
from wsgiref.simple_server import make_server
from cgi import parse_qs, escape
from PIL import Image
import StringIO

html="""<html><body><form method="post">
Name: <input type="text" name="name">
<input type="submit" value="Submit" /></form></body></html>"""

def application(environ, start_response):
    # вивести вміст деяких змінних середовища
    print 'QUERY_STRING:', environ['QUERY_STRING']
    print 'REQUEST_METHOD:', environ['REQUEST_METHOD']
    print 'PATH_INFO:', environ['PATH_INFO']
    print 'HTTP_ACCEPT:', environ['HTTP_ACCEPT']
    
    response_headers=[('Content-Type', 'text/html')] # заголовки
    if environ['REQUEST_METHOD'] == 'GET': # якщо запит GET
        parameters=parse_qs(environ['QUERY_STRING']) # парам. з рядка запиту
        if 'name' in parameters: # якщо в запиті є параметр 'name'
            name = escape(parameters['name'][0]) # його значення
            response_body="<h2>Hello %s </h2>" % (name) # тіло відп.
        elif environ['PATH_INFO']=="/pic.png": # якщо запит на рисунок
            image = Image.new('RGB', (10, 10), (0, 255, 0)) # рисунок
            out=StringIO.StringIO()
            image.save(out, format='PNG') # зберегти в пам'ять
            response_headers = [('Content-Type', 'image/png')] # заголовки
            response_body=out.getvalue() # тіло відп. (дані рисунка)
        else: # якщо інший запит
            response_body=html # тіло відп. (документ HTML з формою)
    
    if environ['REQUEST_METHOD'] == 'POST': # якщо запит POST
        try: # змінна CONTENT_LENGTH може бути пуста або відсутня
            request_body_size = int(environ.get('CONTENT_LENGTH', 0))
        except (ValueError):
            request_body_size = 0
        request_body = environ['wsgi.input'].read(request_body_size) # тіло запиту, передане через форму
        parameters = parse_qs(request_body) # словник параметрів форми
        name = escape(parameters['name'][0]) # значення параметра 'name' 
        response_body='<h2><img src="pic.png" alt="pic">Hello %s </h2>' % (name) # тіло відповіді
    
    start_response('200 OK', response_headers)
    return [response_body]

httpd = make_server('localhost', 80, application) # WSGI сервер
httpd.serve_forever()
"""
    QUERY_STRING: name=Volodymyr
    REQUEST_METHOD: GET
    PATH_INFO: /
    HTTP_ACCEPT: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
![](fig1.png)

Рисунок - Відповідь на запит GET

    QUERY_STRING: 
    REQUEST_METHOD: GET
    PATH_INFO: /
    HTTP_ACCEPT: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
![](fig2.png)

Рисунок - Форма для запиту POST

    QUERY_STRING: 
    REQUEST_METHOD: POST
    PATH_INFO: /
    HTTP_ACCEPT: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    
    QUERY_STRING: 
    REQUEST_METHOD: GET
    PATH_INFO: /pic.png
    HTTP_ACCEPT: */*
![](fig3.png)

Рисунок - Відсилання рисунку
"""
