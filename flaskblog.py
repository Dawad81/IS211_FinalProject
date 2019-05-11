#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring."""


from flask import (Flask, request, session, g, url_for, redirect,
                   render_template, flash)


SECRET_KEY = '.g*lVD?s?hU?Ƅ?'
USERNAME = 'admin'
PASSWORD = 'password'


app = Flask(__name__)
app.config.from_object(__name__)




posts = [
    {
        'author': 'Dennis Awad',
        'title': 'Blog Post #1',
        'content': 'First post of blog material klashfakjhgauhgairhgubrigubariubg',
        'date_posted': 'April 1, 2019'
    },
    {
        'author': 'Nicole Almas',
        'title': 'Blog Post #32',
        'content': 'Second post of blog  material kiboviafpviuanpugnpunpouanb',
        'date_posted': 'April 2, 2019'
    }
]


@app.route("/")
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != USERNAME:
            session['logged_in'] = False
            error = 'The username you entered is incorrect. Please re-enter ' \
                    'a valid username.'
            flash('The username you entered is incorrect. Please re-enter a '
                  'valid username.', 'error')
            return render_template('login.html', error=error)
        elif request.form['password'] != PASSWORD:
            session['logged_in'] = False
            error = 'The password you entered is incorrect. Please re-enter ' \
                    'the valid password for this username.'
            flash('The password you entered is incorrect. Please re-enter '
                  'the valid password for this username.')
            return render_template('login.html', error=error)
        else:
            session['logged_in'] = True
            return redirect('/dashboard')
    else:
        return render_template('login.html', error=error)


@app.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template('home.html', posts=posts, title='Dashboard')


@app.route('/edit', methods=['POST'])
def edit():
    edit_post = request.form['edit']
    #for item in posts:
        #if item['title'] == edit_post:
            #posts.remove(item)
            #return redirect('/dashboard')
    return render_template('edit.html', posts=posts, title='Edit Post')

@app.route('/delete', methods=['POST'])
def delete():
    delete_post = request.form['delete']
    for item in posts:
        if item['title'] == delete_post:
            posts.remove(item)
            return redirect('/dashboard')


@app.route('/addpost', methods=['POST', 'GET'])
def home():
    return render_template('addpost.html', posts=posts, title='Add New Post')


if __name__ == '__main__':
    app.run(debug=True)