from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a2a58d01c94d129e7407823e6faf1ace'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../weblog.db'

db = SQLAlchemy(app)

from weblog import routes
