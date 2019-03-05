# -*- coding: utf-8 -*-
"""
# urllib2 - запити до HTTP серверів
urllib2 модуль містить функції і класи, які допомагають отримувати інформацію за URL переважно від HTTP серверів. Підтримується аутентифікація, переадресація, cookie, проксі-сервера та інше.
"""
import urllib, urllib2
url="http://uk.wikipedia.org/wiki/%D0%9A%D0%BE%D1%81%D1%96%D0%B2"
url=urllib2.unquote(url).decode("utf-8") # перетворити URL в легкий для читання формат
print url
print urllib2.quote(url.encode("utf-8"),safe="%/:=&?~#+!$,;'@()*[]") # перетворити назад

response = urllib2.urlopen('http://httpbin.org/get?name=John') # отримати відповідь за HTTP GET запитом з параметром name=John
#print response.info() # заголовки відповіді у вигляді словника
print response.info()['Content-Type'] # тип тіла відповіді
print response.read(1) # читати 1 байт тіла відповіді
response.close() # закрити файл

form_data = urllib.urlencode({'name':'John'}) # дані для відправлення
headers={'User-Agent' : 'Mozilla 5.0'} # заголовки запиту
request = urllib2.Request('http://httpbin.org/post', form_data, headers) #  HTTP POST запит з даними form_data і заголовками headers
response = urllib2.urlopen(request) # отримати відповідь 
print response.read(1) # читати 1 байт тіла відповіді
