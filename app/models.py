import bcrypt
from app import db
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Integer, ForeignKey, Boolean
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(24), index=True, unique=True)
    first_name = db.Column(db.String(24), index=True)
    last_name = db.Column(db.String(24), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(60))
    profile_picture = db.Column(db.String(140))
    joined = db.Column(DateTime, default=datetime.utcnow, nullable=False)
    events = db.relationship('Event', backref='author', lazy='dynamic')
    
    def set_password(self, password):
        """ Set password. """
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    def check_password(self, password):
        """ Check password. """
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))
    def get_id(self):
       return str(self.user_id) # Return userID as string

    def __repr__(self):
        return '<User {}>'.format(self.username)
    

class Event(db.Model):
    event_id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(140))
    event_description = db.Column(db.String(500))
    thumbnail = db.Column(db.String(40), nullable=False, default='default.jpg')
    created = db.Column(DateTime, default=datetime.utcnow, nullable=False)
    updated = db.Column(DateTime, default=datetime.utcnow, nullable=False)
    event_date = db.Column(DateTime, default=datetime.utcnow, nullable=False)
    event_end = db.Column(DateTime, default=datetime.utcnow, nullable=False)
    event_location = db.Column(db.String(140))
    is_archived = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))


    def __repr__(self):
        return '<Event {}>'.format(self.event_name)