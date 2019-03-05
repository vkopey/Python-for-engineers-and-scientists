# -*- coding: utf-8 -*-
"""
# sqlite3 - DB-API 2.0 інтерфейс для баз даних SQLite
SQLite – це бібліотека, яка реалізує систему керування реляційними базами даних. Підтримує транзакції, не потребує інсталяції, створена мовою C, швидка, не залежить від платформи. Взаємодія з базою даних відбувається мовою SQL. Модуль sqlite3 є інтерфейсом Python до SQLite.
"""
import sqlite3
conn = sqlite3.connect('mysqlite3.db') # об'єкт бази даних
cur = conn.cursor() # об'єкт курсор - виконує запити і отримує результати
# виконати команду SQL, яка створює таблицю з полями name і content
cur.execute('CREATE TABLE IF NOT EXISTS pages(name TEXT, content TEXT)')
conn.commit() # зберегти зміни
# база даних блокується поки транзакція не виконається

name=u"Іванов"
content=u"1990"
# виконати команду SQL, яка додає рядок з даними name,content в таблицю
cur.execute('INSERT INTO pages (name,content) VALUES(?,?)', (name,content))
conn.commit() # зберегти зміни

# виконати команду SQL, яка оновлює дані
cur.execute('UPDATE pages SET content=? WHERE name=?', (content,name))
conn.commit() # зберегти зміни

# виконати команду SQL, яка отримує результати запиту
cur.execute('SELECT content FROM pages WHERE name=?', (name,))
#print cur.fetchone() # отримати наступний рядок множини результату запиту, або
print cur.fetchall() # отримати усі рядки множини результату запиту

cur.close() # закрити курсор
conn.close() # закрити базу даних
