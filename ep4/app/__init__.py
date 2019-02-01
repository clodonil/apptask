import os
from flask import Flask, flash,Blueprint, redirect,url_for,request, render_template
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
             flash('Database criado com sucesso')
             return redirect(url_for('login.auth'))
          else:
             flash("Token invalido, digite para criacao do token nao confere!!!")
             return render_template('settings.html')
       elif request.method == "GET":
          return render_template('settings.html')    
    else:
      return redirect(url_for('login.auth'))

# Modulos
from app import model
from app.cadastro import cadastro
from app.login    import login

app.register_blueprint(cadastro, url_prefix='/cadastro')
app.register_blueprint(login,    url_prefix='/login'   )