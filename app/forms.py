from app.models import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, ValidationError, EqualTo


class LoginForm(FlaskForm):
    """ Login form. """
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
    """ Registration form. """
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Register")

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user is not None:
            raise ValidationError(
                "this username is taken, please use a different username")
        
    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user is not None:
            raise ValidationError(
                "this email is taken, please use a different email")
        

class EventForm(FlaskForm):
    """ Event form. """
    event_name = StringField('Event Name', validators=[DataRequired()])
    event_description = StringField('Event Description', validators=[DataRequired()])
    thumbnail = StringField('Thumbnail', validators=[DataRequired()])
    event_date = StringField('Event Date', validators=[DataRequired()])
    event_end = StringField('Event End', validators=[DataRequired()])
    event_location = StringField('Event Location', validators=[DataRequired()])
    submit = SubmitField('Create Event')
