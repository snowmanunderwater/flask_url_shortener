import os

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SECRET_KEY = 'testkey'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'flask-url-shortener.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True

del os