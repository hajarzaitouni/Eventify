from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import User, Event
from app.forms import LoginForm, RegisterForm, EventForm


@app.route('/')
@app.route('/home')
def home():
    """ Home page route. """
    return render_template('home.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    """ Login route. """
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            return redirect(url_for('login'))
        return redirect(url_for('home'))
    return render_template('login.html', title='Sign In', form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    """ Register route. """
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)