from app.models import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateTimeLocalField
from wtforms.validators import DataRequired, Email, ValidationError, EqualTo
from flask_wtf.file import FileField, FileAllowed


class LoginForm(FlaskForm):
    """ Login form. """
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
    """ Registration form. """
    username = StringField('Username', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(),
                                                 EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        """ Validate username. """
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please choose a different username.')
        
    def validate_email(self, email):
        """ Validate email. """
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')
        

class EventForm(FlaskForm):
    """ Event form. """
    event_name = StringField('Event Name', validators=[DataRequired()], render_kw={"autocomplete": "off"})
    event_description = StringField('Event Description', validators=[DataRequired()], render_kw={"autocomplete": "off"})
    thumbnail = FileField("Update Picture", validators=[FileAllowed(["jpg", "png", "jpeg"])])
    event_date = DateTimeLocalField('Event Date', format='%Y-%m-%dT%H:%M', validators=[DataRequired()])
    event_end = DateTimeLocalField('Event End', format='%Y-%m-%dT%H:%M', validators=[DataRequired()])
    event_location = StringField('Event Location', validators=[DataRequired()], render_kw={"autocomplete": "off"})
    submit = SubmitField('Create Event')

class UpdateEventForm(FlaskForm):
    """ Update event form. """
    event_name = StringField('Event Name', render_kw={"autocomplete": "off"})
    event_description = StringField('Event Description', render_kw={"autocomplete": "off"})
    thumbnail = FileField("Update Picture", validators=[FileAllowed(["jpg", "png", "jpeg"])])
    event_date = DateTimeLocalField('Event Date', format='%Y-%m-%dT%H:%M')
    event_end = DateTimeLocalField('Event End', format='%Y-%m-%dT%H:%M')
    event_location = StringField('Event Location', render_kw={"autocomplete": "off"})
    submit = SubmitField('Update Event')

class archiveEventForm(FlaskForm):
    """ Archive event form. """
    event_name = StringField('Event Name', render_kw={"autocomplete": "off"})
    event_description = StringField('Event Description', render_kw={"autocomplete": "off"})
    thumbnail = FileField("Update Picture", validators=[FileAllowed(["jpg", "png", "jpeg"])])
    event_date = DateTimeLocalField('Event Date', format='%Y-%m-%dT%H:%M')
    event_end = DateTimeLocalField('Event End', format='%Y-%m-%dT%H:%M')
    event_location = StringField('Event Location', render_kw={"autocomplete": "off"})
    submit = SubmitField('Archive Event')