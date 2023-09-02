import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'admin'
    SQLALCHEMY_DATABASE_URI = 'mysql://admin:admin@localhost:5306/trabalho'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
