from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

class Config:
    SECRET_KEY = 'admin'
    SQLALCHEMY_DATABASE_URI = 'mysql://admin:admin@localhost:5306/trabalho'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)