import os

WTF_CSRF_ENABLED=True
SECRET_KEY = "you-will-never-guess"


basedir = os.path.abspath(os.path.dirname(__file__))

database = os.path.join(basedir, 'db/banco_de_dados.db')

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + database

SQLALCHEMY_TRACK_MODIFICATIONS = False


DEBUG = True

PORT = 8080
HOST = "0.0.0.0"

create_db_token = "macacoloco"
