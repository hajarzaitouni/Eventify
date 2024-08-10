from flask import render_template, request, redirect
from app import app
from app import db

@app.route('/')
@app.route('/home')
def home():
    """ Home page route. """
    return 'Hello World!'
