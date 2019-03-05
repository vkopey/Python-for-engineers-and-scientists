# -*- coding: utf-8 -*-
"""
# CGI HTTP сервер
Веб-сервер — це програма, яка приймає HTTP-запити від клієнтів (зазвичай веб-браузерів) і видає їм HTTP-відповіді, як правило, з HTML-сторінкою. Протокол передачі гіпертексту HTTP описує HTTP-повідомлення, які складаються з стартового рядка (тип повідомлення), заголовків (параметри транзакції HTTP) і необов'язкового тіла (наприклад з даними HTML). HTTP-повідомлення можна переглянути, наприклад, в браузері Firefox 61 в меню веб-розробка/мережа. Приклад HTTP-запиту типу GET до ресурсу /hello.html.

    GET /hello.html HTTP/1.1
    Host: localhost
    (пустий рядок)

Метод GET використовується для запиту вмісту вказаного ресурсу, а метод POST - для передачі даних вказаному ресурсу. Приклад HTTP-відповіді сервера з кодом стану 200 (виконано):

    HTTP/1.0 200 OK
    Content-type: text/html
    (пустий рядок)
    <html><body>Hello</body></html>

В прикладі створено `BaseHTTPServer.HTTPServer` сервер з підтримкою  запитів GET, HEAD, POST і CGI-програм. В даному випадку усі CGI-програми повинні бути розташовані в каталозі cgi поряд з сервером. Запустіть сервер та в адресному рядку браузера введіть:

    http://localhost/hello.html
"""
import os, sys
import BaseHTTPServer, CGIHTTPServer
with open('hello.html', 'w') as f: # створити документ HTML
    f.write("<html><body>Hello</body></html>")
class Handler(CGIHTTPServer.CGIHTTPRequestHandler): # обробник запитів
    cgi_directories = ["/cgi"] # каталог з CGI-програмами
srvraddr = ('localhost', 80) # ім'я хоста, номер порта
srvrobj = BaseHTTPServer.HTTPServer(srvraddr, Handler) # сервер
srvrobj.serve_forever() # обслуговувати клієнтів до завершення
"""
![](fig.png)

Рисунок - Результати роботи сервера
"""
