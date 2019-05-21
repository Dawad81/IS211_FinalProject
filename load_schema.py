
import sqlite3 as lite
import datetime


CON = lite.connect('post.db')

with CON:
    cur = CON.cursor()
    cur.execute("DROP TABLE IF EXISTS authors")
    cur.execute("CREATE TABLE authors(user_id INTEGER PRIMARY KEY ASC, first_"
                "name TEXT, last_name TEXT, username TEXT, password TEXT)")
    cur.execute("INSERT INTO authors (user_id, first_name, last_name, "
                "username, password) VALUES (01, 'Dennis', 'Awad', 'Dawad', "
                "'sassmasterd')")
    cur.execute("INSERT INTO authors (user_id, first_name, last_name, "
                "username, password) VALUES (02, 'Nicole', 'Almas', 'Nalmas', "
                "'MrsAwad')")
    cur.execute("INSERT INTO authors (user_id, first_name, last_name, "
                "username, password) VALUES (03, 'Future', 'Awad', 'Fawad', "
                "'KidAwad')")
    cur.execute("DROP TABLE IF EXISTS blogpost")
    cur.execute("CREATE TABLE blogpost (blog_id INTEGER PRIMARY KEY ASC, title "
                "TEXT, content INTEGER, date TEXT, category TEXT)")
    cur.execute(
        "INSERT INTO blogpost (blog_id, title, content, date, category) "
        "VALUES (?, ?, ?, ?, ?)", (
            01, 'test blog', 'This is to test posting the first blog in '
                             'the data base',
            datetime.datetime.now(), 'testing'))
    cur.execute(
        "INSERT INTO blogpost (blog_id, title, content, date, category) "
        "VALUES (?, ?, ?, ?, ?)", (
            02, 'test blog nicole', 'This is to test posting the first '
                                    'blog from nicole',
            datetime.datetime.now(), 'testing'))
    cur.execute(
        "INSERT INTO blogpost (blog_id, title, content, date, category) "
        "VALUES (?, ?, ?, ?, ?)", (
            03, 'test blog Fawad', 'This is to test posting the first '
                                   'unpublished blog from Future',
            datetime.datetime.now(), 'testing'))
    cur.execute(
        "INSERT INTO blogpost (blog_id, title, content, date, category) "
        "VALUES (?, ?, ?, ?, ?)", (
            04, 'test blog Fawad', 'This is to test posting the first '
                                   'published blog from Future',
            datetime.datetime.now(),'testing'))
    cur.execute("DROP TABLE IF EXISTS published")
    cur.execute("CREATE TABLE published(user_id INTEGER, blog_id INTEGER, "
                "published INTEGER)")
    cur.execute("INSERT INTO published (user_id, blog_id, published) "
                "VALUES (01,01,01)")
    cur.execute("INSERT INTO published (user_id, blog_id, published) "
                "VALUES (02,02,01)")
    cur.execute("INSERT INTO published (user_id, blog_id, published) "
                "VALUES (03,03,0)")
    cur.execute("INSERT INTO published (user_id, blog_id, published) "
                "VALUES (03,04,1)")
