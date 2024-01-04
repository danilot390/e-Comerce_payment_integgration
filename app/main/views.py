from flask import render_template

from . import main

@main.route('/home')
def home():
    context ={
    }
    return render_template('index.html', **context)

    