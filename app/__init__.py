from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

#create secret key for cookies using secrets module secrets.token_hex(16)
app.config['SECRET_KEY'] = '237f9721b57d0f0b25b363a353debf31'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:rootroot@localhost/eventify'


db = SQLAlchemy(app)

from app import routes