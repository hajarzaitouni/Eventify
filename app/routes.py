from flask import render_template, request, redirect
from app import app , db
from app.models import User, Event

@app.route('/')
@app.route('/home')
def home():
    """ Home page route. """
    return render_template('home.html')
