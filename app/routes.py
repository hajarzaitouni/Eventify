from flask import render_template, request, redirect
from app import app


@app.route('/')
@app.route('/home')
def home():
    """ Home page route. """
    return render_template('home.html')
