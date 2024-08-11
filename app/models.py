from app import db
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Integer, ForeignKey, Boolean

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(24), index=True, unique=True)
    first_name = db.Column(db.String(24), index=True)
    last_name = db.Column(db.String(24), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(140))
    profile_picture = db.Column(db.String(140))
    joined = db.Column(DateTime, default=datetime.utcnow, nullable=False)
    events = db.relationship('Event', backref='author', lazy='dynamic')
    
    def __repr__(self):
        return '<User {}>'.format(self.username)
    

class Event(db.Model):
    event_id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(140))
    event_description = db.Column(db.String(500))
    thumbnail = db.Column(db.String(140))
    created = db.Column(DateTime, default=datetime.utcnow, nullable=False)
    updated = db.Column(DateTime, default=datetime.utcnow, nullable=False)
    event_date = db.Column(DateTime, default=datetime.utcnow, nullable=False)
    event_end = db.Column(DateTime, default=datetime.utcnow, nullable=False)
    event_location = db.Column(db.String(140))
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))

    def __repr__(self):
        return '<Event {}>'.format(self.event_name)