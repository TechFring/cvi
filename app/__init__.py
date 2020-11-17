from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from app.helpers.file import load_config


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/database_cvi'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'secret'

config = load_config()

# configurando o flask mail
app.config['MAIL_SERVER'] = config['MAIL_SERVER']
app.config['MAIL_PORT'] = config['MAIL_PORT']
app.config['MAIL_USERNAME'] = config['MAIL_USERNAME']
app.config['MAIL_PASSWORD'] = config['MAIL_PASSWORD']
app.config['MAIL_USE_TLS'] = config['MAIL_USE_TLS']
app.config['MAIL_USE_SSL'] = config['MAIL_USE_SSL']

mail = Mail(app)

UPLOAD_FOLDER = 'app/static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

login_manager = LoginManager(app)
db = SQLAlchemy(app)
