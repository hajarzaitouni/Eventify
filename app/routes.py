from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.models import User, Event
from app.forms import LoginForm, RegisterForm, EventForm


@app.route('/')
@app.route('/home')
def home():
    """ Home page route. """
    form = LoginForm()
    return render_template('home.html', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    """ Login route. """
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password', 'danger')
            print('Flash message set')
            return redirect(url_for('login'))
        flash('Login successful', 'success')
        print('Redirecting to event_dashboard')
        return redirect(url_for('event_dashboard'))
    return render_template('login.html', title='Sign In', form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    """ Register route. """
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,
                    email=form.email.data,
                    first_name=form.first_name.data,
                    last_name=form.last_name.data)
        user.set_password(form.password.data)
        try:
            db.session.add(user)
            db.session.commit()
            flash('Congratulations, you are now a registered user!')
        except Exception as e:
            flash("Error adding user to the database")
            db.session.rollback()
            return render_template('register.html', title='Register', form=form, error="Registration failed.")
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/event", methods=['GET', 'POST'])
def event_dashboard():
    """ Event dashboard route. """
    return render_template('event_dashbord.html')