from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a2a58d01c94d129e7407823e6faf1ace'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../weblog.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from weblog import routes
