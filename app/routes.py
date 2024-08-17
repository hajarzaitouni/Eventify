from flask import render_template, request, redirect, url_for, flash, jsonify
from app import app, db, allowed_file
from app.models import User, Event
from app.forms import LoginForm, RegisterForm, EventForm, UpdateEventForm, archiveEventForm
from flask_login import current_user, login_user, logout_user, login_required
from app.helper import save_picture, delete_picture
from werkzeug.utils import secure_filename
import os


@app.route('/')
@app.route('/home')
def home():
    """ Home page route. """
    login_form = LoginForm()
    register_form = RegisterForm()
    return render_template('home.html', login_form=login_form, register_form=register_form,title='Home')


@app.route("/login", methods=['GET', 'POST'])
def login():
    """ Login route. """
    if current_user.is_authenticated:
        return redirect(url_for('event_dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            data = {'success': False, 'message': 'Invalid username or password!'}
            return jsonify(data)
        login_user(user) # Log the user in
        return jsonify({'success': True, 'message': 'Login successful!'})
    return jsonify({'success': False, 'message': 'Form validation failed!'})

@app.route("/register", methods=['GET', 'POST'])
def register():
    """ Register route. """
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        password = form.password.data
        user = User(username=username,
                    email=email,
                    first_name=first_name,
                    last_name=last_name)
        user.set_password(password)
        try:
            db.session.add(user)
            db.session.commit()
            return jsonify({'success': True, 'message': 'Registration successful!'})
        except Exception as e:
            db.session.rollback()
            return jsonify({'success': False, 'message': 'Registration failed!. Please try again.'})
    
    return jsonify({'success': False, 'message': 'Form validation failed!'})

@app.route("/logout")
def logout():
    """ Logout route. """
    logout_user()
    return redirect(url_for('home'))

@app.route("/event", methods=['GET', 'POST'])
@login_required
def event_dashboard():
    """ Event dashboard route. """
    form = EventForm()
    
    EventUser = Event.query.filter_by(user_id=current_user.user_id, is_archived=False).all()
    username = current_user.username
    
    return render_template('event_dashboard.html', form=form, title='Event', username=username, events=EventUser)


@app.route("/event/archive", methods=['GET'])
@login_required
def show_archived_events():
    """ Show all archived events. """
    archived_events = Event.query.filter_by(user_id=current_user.user_id, is_archived=True).all()
    return render_template('archive_event.html', title='Archived Events', events=archived_events)


@app.route('/event/create', methods=['GET', 'POST'])
def create_event():
    form = EventForm()
    thumbnail_gen = 'path/to/default/image.jpg'  # Replace with the path to your default image
    if form.validate_on_submit():
        # Handle file upload
        file = form.thumbnail.data
        if file and allowed_file(file.filename):
            filename = save_picture(file)
            print(f"File saved as: {filename}")
            thumbnail_gen = url_for("static", filename = "images/thumbnail_pics/" + filename)
            
            # Save the file path to the database
            event = Event(
                event_name=form.event_name.data,
                event_date=form.event_date.data,
                event_end=form.event_end.data,
                event_location=form.event_location.data,
                event_description=form.event_description.data,
                thumbnail=filename,
                user_id=current_user.user_id
            )
            db.session.add(event)
            db.session.commit()
            flash('Event created successfully!', 'success')
            print('Event created successfully')
            return redirect(url_for('event_dashboard'))
        elif not form.thumbnail.data:
            event = Event(
                event_name=form.event_name.data,
                event_date=form.event_date.data,
                event_end=form.event_end.data,
                event_location=form.event_location.data,
                event_description=form.event_description.data,
                user_id=current_user.user_id
            )
            db.session.add(event)
            db.session.commit()
            flash('Event created successfully!', 'success')
            print('Event created successfully')
            return redirect(url_for('event_dashboard'))
        else:
            flash('Invalid file type.', 'danger')
    return render_template('event_dashboard.html', form=form, thumbnail=thumbnail_gen, title='Create Event')


@app.route("/event/delete/<int:event_id>", methods=['GET', 'POST'])
@login_required
def delete_event(event_id):
    """ Delete event. """
    event = Event.query.filter_by(event_id=event_id).first()
    if event.user_id == current_user.user_id:
        if event is not None:
            if event.thumbnail and event.thumbnail != 'default.jpg':
                delete_picture(event.thumbnail)
            db.session.delete(event)
            db.session.commit()
            flash('Event deleted.')
        else:
            flash('Event not found.')
    return redirect(url_for('event_dashboard'))
    


@app.route("/event/update/<int:event_id>", methods=['GET', 'POST'])
@login_required
def update_event(event_id):
    """ Update event. """
    event = Event.query.filter_by(event_id=event_id).first()
    form = UpdateEventForm()
    if form.validate_on_submit():
        event.event_name = form.event_name.data
        event.event_description = form.event_description.data
        event.event_location = form.event_location.data
        event.event_date = form.event_date.data
        event.event_end = form.event_end.data
        db.session.commit()
        flash('Event updated.')
        return redirect(url_for('event_dashboard'))
    elif request.method == 'GET':
        form.event_name.data = event.event_name
        form.event_description.data = event.event_description
        form.event_location.data = event.event_location
        form.event_date.data = event.event_date
        form.event_end.data = event.event_end
    return render_template('update_event.html', title='Update Event', form=form, event_id=event_id)

@app.route("/event/archive/<int:event_id>", methods=['POST'])
@login_required
def archive_event(event_id):
    """ Archive event. """
    event = Event.query.get_or_404(event_id)
    if event.is_archived == True:
        event.is_archived = False
        flash('Event unarchived.')
    else:
        event.is_archived = True
        flash('Event archived.')
    db.session.commit()
    return redirect(url_for('event_dashboard'))



# @app.route("/event/unarchive", methods=['GET', 'POST'])