from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a2a58d01c94d129e7407823e6faf1ace'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../LoginModule.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Please login as first step'
login_manager.login_message_category = 'info'

from Weblog import routes
