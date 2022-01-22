import sqlite3

connection = sqlite3.connect('database.db')

with open('scheme.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute('insert into posts (title, content) VALUES  (?, ?)',
            ('Пост 1', "Текст поста"))

cur.execute('insert into posts (title, content) VALUES  (?, ?)',
            ('Пост 2', "Текст поста"))

cur.execute('insert into posts (title, content) VALUES  (?, ?)',
            ('Пост 3', "Текст поста"))
connection.commit()
connection.close()
