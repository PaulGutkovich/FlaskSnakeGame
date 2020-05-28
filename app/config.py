import os

DEBUG = False

class Config(object):
    SECRET_KEY = os.urandom(64) if DEBUG else 'secret'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///../app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False