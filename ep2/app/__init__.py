from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

# Banco de Dados
db = SQLAlchemy(app)

# Modulos
from app import model
