#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring."""


import datetime
import sqlite3

from flask import (Flask, request, session, g, url_for, redirect,
                   render_template, flash)
from flask_bootstrap import Bootstrap

DATABASE = 'post.db'
SECRET_KEY = '.g*lVD?s?HU?Ƅ?'



app = Flask(__name__)
Bootstrap(app)
app.config.from_object(__name__)


@app.before_request
def before_request():
    g.db = get_db()


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'GET':
        blogpost_info = g.db.execute('SELECT * FROM blogpost ORDER BY date DESC')
        posts = []
        for row in blogpost_info:
            posts.append(
                {'blog_id': row[0], 'title': row[1], 'content': row[2], 'date': row[3], 'category': row[4]})
        return render_template('home.html', posts=posts, title='Home')
    elif request.method == 'POST':
        return redirect('/login')


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        htmlusername = request.form['username']
        htmlpassword = request.form['password']
        author_info = g.db.execute('SELECT * FROM authors WHERE username = ?', (htmlusername,))
        author = [dict(user_id=row[0], first_name=row[1], last_name=row[2], username=row[3], password=row[4])for row in author_info.fetchall()]
        if not author:
            flash('Username entered is invalid! Please re-enter a valid username.', error)
            return redirect('/login')
        if htmlpassword != author[0]['password']:
            flash('Password enter is invalid! Please re-enter a valid password for {}'.format(htmlusername))
            return redirect('/login')
        else:
            session['logged_in'] = True
            session['username'] = htmlusername
            session['password'] = htmlpassword
            return redirect('/dashboard')
    else:
        return render_template('login.html', error=error)



@app.route('/dashboard', methods=['GET'])
def dashboard():
    if session['logged_in'] == False:
        flash("You are not logged in! Please login to access the site.",
              'error')
        return redirect(url_for('login'))
    else:
        if request.method == 'GET':
            author_info = g.db.execute('SELECT * FROM authors WHERE username = ?', (session['username'],))
            author = [dict(user_id=row[0], first_name=row[1], last_name=row[2], username=row[3], password=row[4]) for row in author_info.fetchall()]
            author_name = author[0]['first_name'] + ' ' + author[0]['last_name']
            user_id_num = author[0]['user_id']
            published_info = g.db.execute('SELECT * FROM published WHERE user_id = ?', (user_id_num,))
            published = [i for i in published_info.fetchall()]
            published_list = [i[1] for i in published]
            posts = []
            for item in published_list:
                blogpost_info = g.db.execute('SELECT * FROM blogpost WHERE blog_id = ?', (item,))
                for row in blogpost_info:
                    posts.append(
                        {'blog_id': row[0], 'title': row[1], 'content': row[2], 'date': row[3], 'category': row[4]})
            return render_template('dashboard.html', posts=posts, author_name=author_name, title='Dashboard')


@app.route('/edit', methods=['POST', 'GET'])
def edit():
    if session['logged_in'] == False:
        flash("You are not logged in! Please login to access the site.",
              'error')
        return redirect(url_for('login'))
    else:
        if request.method == 'POST':
            timestamp = datetime.datetime.now()
            author_info = g.db.execute('SELECT * FROM authors WHERE username = ?', (session['username'],))
            author = [dict(user_id=row[0], first_name=row[1], last_name=row[2], username=row[3], password=row[4]) for row in author_info.fetchall()]
            print 'authordict=', author

            author_name = author[0]['first_name'] + ' ' + author[0]['last_name']
            print 'authorname=' + author_name
            user_id_num = author[0]['user_id']
            print 'useridnum=', user_id_num
            published_info = g.db.execute('SELECT * FROM published WHERE user_id = ?', (user_id_num,))
            print published_info
            published = [i for i in published_info.fetchall()]
            print 'published=', published
            published_list = [i[1] for i in published]
            print 'publishedlist=', published_list
            posts = []
            for item in published_list:
                blogpost_info = g.db.execute('SELECT * FROM blogpost WHERE blog_id = ?', (item,))
                print blogpost_info
                for row in blogpost_info:
                    posts.append(
                        {'blog_id': row[0], 'title': row[1], 'content': row[2], 'date': row[3], 'category': row[4]})
                print posts
            edit_post = request.form['edit']
            return render_template('edit.html', edit_post=edit_post, posts=posts, author_name=author_name, title='Edit Post', timestamp=timestamp)


@app.route('/editpost', methods=['POST', 'GET'])
def editpost():
    if session['logged_in'] == False:
        flash("You are not logged in! Please login to access the site.",
              'error')
        return redirect(url_for('login'))
    else:
        if request.method == 'POST':
            timestamp = datetime.datetime.now()
            author_info = g.db.execute('SELECT * FROM authors WHERE username = ?', (session['username'],))
            author = [dict(user_id=row[0], first_name=row[1], last_name=row[2], username=row[3], password=row[4]) for
                      row in author_info.fetchall()]
            print 'authordict=', author
            author_name = author[0]['first_name'] + ' ' + author[0]['last_name']
            user_id_num = author[0]['user_id']
            g.db.execute('UPDATE blogpost SET content=?,date=? Where content=?',(request.form['content'], timestamp, request.form['del']))
            g.db.commit()
            return redirect('/dashboard')


@app.route('/delete', methods=['POST'])
def delete():
    if session['logged_in'] == False:
        flash("You are not logged in! Please login to access the site.",
              'error')
        return redirect(url_for('login'))
    else:
        delete_post = request.form['delete']
        timestamp = datetime.datetime.now()
        author_info = g.db.execute('SELECT * FROM authors WHERE username = ?', (session['username'],))
        author = [dict(user_id=row[0], first_name=row[1], last_name=row[2], username=row[3], password=row[4]) for
                  row in author_info.fetchall()]
        print 'authordict=', author
        author_name = author[0]['first_name'] + ' ' + author[0]['last_name']
        print 'authorname=' + author_name
        user_id_num = author[0]['user_id']
        print 'useridnum=', user_id_num

        blogpost_info = g.db.execute('SELECT * FROM blogpost WHERE content=?', (delete_post,))
        posts = []
        for row in blogpost_info:
            posts.append(
                {'blog_id': row[0], 'title': row[1], 'content': row[2], 'date': row[3], 'category': row[4]})
        print 'this is post=', posts
        blog_id_num = posts[0]['blog_id']
        print 'blogidnum=', blog_id_num
        g.db.execute('DELETE FROM blogpost WHERE content = ?', (delete_post,))
        g.db.commit()
        g.db.execute('DELETE FROM published Where blog_id=?', (blog_id_num,))
        g.db.commit()
        return redirect('/dashboard')


@app.route('/addpost', methods=['POST', 'GET'])
def addpost():
    if session['logged_in'] == False:
        flash("You are not logged in! Please login to access the site.",
              'error')
        return redirect(url_for('login'))
    else:
            return render_template('addpost.html', title='Add New Post')


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if session['logged_in'] == False:
        flash("You are not logged in! Please login to access the site.",
              'error')
        return redirect(url_for('login'))
    else:
        if request.method == 'POST':
            if not request.form['title']:
                flash("Title field empty. Please enter title and re-submit")
                return redirect(url_for('addpost'))
            elif request.form['content'] == "":
                flash('Blog post field empty. Please enter Blog post and re-submit')
                return redirect(url_for('addpost'))

            else:
                timestamp = datetime.datetime.now()
                author_info = g.db.execute('SELECT * FROM authors WHERE username = ?', (session['username'],))
                author = [dict(user_id=row[0], first_name=row[1], last_name=row[2], username=row[3], password=row[4])
                          for
                          row in author_info.fetchall()]
                print 'authordict=', author

                author_name = author[0]['first_name'] + ' ' + author[0]['last_name']
                print 'authorname=' + author_name
                user_id_num = author[0]['user_id']
                print 'useridnum=', user_id_num

                g.db.execute('INSERT INTO blogpost (title, content, date, category) VALUES (?,?,?,?)',
                             (request.form['title'], request.form['content'], timestamp, request.form['category']))
                g.db.commit()
                blogpost_info = g.db.execute('SELECT * FROM blogpost WHERE content=?', (request.form['content'],))
                posts = []
                for row in blogpost_info:
                    posts.append(
                        {'blog_id': row[0], 'title': row[1], 'content': row[2], 'date': row[3], 'category': row[4]})
                print 'this is post=', posts
                blog_id_num = posts[0]['blog_id']
                print 'blogidnum=', blog_id_num

                g.db.execute('INSERT INTO published (user_id, blog_id, published) VALUES (?,?,?)',
                             (user_id_num, blog_id_num, 01))
                g.db.commit()

                return redirect('/dashboard')


if __name__ == '__main__':
    app.run(debug=True)