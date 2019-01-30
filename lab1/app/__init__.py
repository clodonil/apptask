from flask import Flask
import os
from flask import Flask, Blueprint, redirect,url_for
from flask.ext.sqlalchemy import SQLAlchemy
from config import basedir


app = Flask(__name__)
app.config.from_object('config')


# Banco de Dados
db = SQLAlchemy(app)

# Modulos
from app import model
