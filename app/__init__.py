from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
import os


app = Flask(__name__)

#create secret key for cookies using secrets module secrets.token_hex(16)
app.config['SECRET_KEY'] = '237f9721b57d0f0b25b363a353debf31'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL") or \
    'mysql://root:rootroot@localhost/Eventify'


db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
migrate = Migrate(app, db)

from app import routes, models

@login_manager.user_loader
def load_user(user_id):
    return models.User.query.get(int(user_id))