from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os


app = Flask(__name__)

#create secret key for cookies using secrets module secrets.token_hex(16)
app.config['SECRET_KEY'] = '237f9721b57d0f0b25b363a353debf31'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL") or \
    'mysql://root:rootroot@localhost/Eventify'

# UPLOAD_FOLDER = "static/images/thumbnail_pics"
# app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# ALLOWED_EXTENSIONS = {"jpg", "png", "jpeg"}

# Set the upload folder configuration
UPLOAD_FOLDER = os.path.join(app.root_path, 'static/images/thumbnail_pics')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']




db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = "login"




from app.models import User, Event
# Define user_loader function
@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from app import routes, models
