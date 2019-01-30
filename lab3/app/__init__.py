import os
from flask import Flask, Blueprint, redirect,url_for,request, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from config import database, create_db_token


app = Flask(__name__)
app.config.from_object('config')


# Banco de Dados
db = SQLAlchemy(app)

# Basic Routes #

@app.route('/',methods = ["GET","POST"])
def index():
    if not os.path.exists(database):
       if request.method == "POST":
          get_token = request.form['token']
          if create_db_token == get_token:
             db.create_all()
             return "<h1>Database criado com sucesso.</h1>"
          else:
             return "<h1> Token para criacao do token nao confere </h1>"
       elif request.method == "GET":
          return render_template('settings.html')    

# Modulos
from app import model
from app.cadastro import cadastro
from app.login    import login

app.register_blueprint(cadastro, url_prefix='/cadastro')
app.register_blueprint(login,    url_prefix='/login'   )