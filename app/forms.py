from app.models import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField
from wtforms.validators import DataRequired, Email, ValidationError, Length


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
    event_name = StringField('Event Name', validators=[DataRequired()])
    event_description = StringField('Event Description', validators=[DataRequired()])
    thumbnail = StringField('Thumbnail', validators=[DataRequired()])
    event_date = DateField('Event Date', format='%d-%m-%Y', validators=[DataRequired()])
    event_end = DateField('Event End', format='%d-%m-%Y', validators=[DataRequired()])
    event_location = StringField('Event Location', validators=[DataRequired()])
    submit = SubmitField('Create Event')