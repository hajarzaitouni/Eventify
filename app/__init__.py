from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask_login import LoginManager
import os


app = Flask(__name__)

#create secret key for cookies using secrets module secrets.token_hex(16)
app.config['SECRET_KEY'] = '237f9721b57d0f0b25b363a353debf31'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL") or \
    'mysql://root:rootroot@localhost/Eventify'


db = SQLAlchemy(app)
migrate = Migrate(app, db)
# login = LoginManager(app)

from app import routes, models
