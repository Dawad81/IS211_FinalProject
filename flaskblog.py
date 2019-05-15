#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring."""

import os
import pickle
from flask import (Flask, request, session, g, url_for, redirect,
                   render_template, flash)
#from flask_sqlalchemy import SQLAlchemy


SECRET_KEY = '.g*lVD?s?hU?Ƅ?'
USERNAME = 'admin'
PASSWORD = 'password'


app = Flask(__name__)
app.config.from_object(__name__)

#TODO revers cronological order
# re work rout url table
# then after log in be able to make changes,
# implement sqlite3 as data base
# work on boot strap/css


# posts = [
#     {
#         'author': 'Dennis Awad',
#         'title': 'Blog Post #1',
#         'content': 'First post of blog material klashfakjhgauhgairhgubrigubariubg',
#         'date_posted': 'April 1, 2019'
#     },
#     {
#         'author': 'Nicole Almas',
#         'title': 'Blog Post #32',
#         'content': 'Second post of blog  material kiboviafpviuanpugnpunpouanb',
#         'date_posted': 'April 2, 2019'
#     }
# ]


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
    if session['logged_in'] == False:
        flash("You are not logged in! Please login to access the site.",
              'error')
        return redirect(url_for('login'))
    else:
        return render_template('home.html', posts=posts, title='Dashboard')


@app.route('/edit', methods=['POST', 'GET'])
def edit():
    if session['logged_in'] == False:
        flash("You are not logged in! Please login to access the site.",
              'error')
        return redirect(url_for('login'))
    else:
        if request.method == 'POST':
            edit_post = request.form['edit']
            return render_template('edit.html', edit_post=edit_post, posts=posts, title='Edit Post')


@app.route('/editpost', methods=['POST', 'GET'])
def editpost():
    if session['logged_in'] == False:
        flash("You are not logged in! Please login to access the site.",
              'error')
        return redirect(url_for('login'))
    else:
        if request.method == 'POST':
            to_pickle_file = open('posts.pkl', 'wb')
            posts.append({'author': request.form['author'],
                          'title': request.form['title'],
                          'content': request.form['content'],
                          'date': request.form['date']})
            pickle.dump(posts, to_pickle_file)
            to_pickle_file.close()

            delete_post = request.form['del']
            for item in posts:
                if item['content'] == delete_post:
                    posts.remove(item)
                    to_pickle_file = open('posts.pkl', 'wb')
                    pickle.dump(posts, to_pickle_file)
                    to_pickle_file.close()
            return redirect('/dashboard')




@app.route('/delete', methods=['POST'])
def delete():
    if session['logged_in'] == False:
        flash("You are not logged in! Please login to access the site.",
              'error')
        return redirect(url_for('login'))
    else:
        delete_post = request.form['delete']
        for item in posts:
            if item['content'] == delete_post:
                posts.remove(item)
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
def submit():#Todo this is not recognizing empty feilds
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
            elif request.form['date'] == "":
                flash('Date field empty. Please enter a valid date and re-submit.')
                return redirect(url_for('addpost'))
            else:
                to_pickle_file = open('posts.pkl', 'wb')
                posts.append({'author': request.form['author'],
                              'title': request.form['title'],
                              'content': request.form['content'],
                              'date': request.form['date']})
                pickle.dump(posts, to_pickle_file)
                to_pickle_file.close()
                return redirect(url_for('dashboard'))


@app.route('/save', methods=['POST'])
def save():
    to_pickle_file = open('posts.pkl', 'wb')
    pickle.dump(posts, to_pickle_file)
    to_pickle_file.close()
    return redirect('/dashboard')


def get_posts():
    from_pickle_file = 'posts.pkl'
    if os.path.exists(from_pickle_file):
        posts = pickle.load(open(from_pickle_file, 'rb'))
        return posts
    else:
        posts = []
        return posts

if __name__ == '__main__':
    posts = get_posts()
    app.run(debug=True)
