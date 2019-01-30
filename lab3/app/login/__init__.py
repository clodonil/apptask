from flask import render_template,  Blueprint, request
from app.model  import People



login = Blueprint('login',__name__)


@login.route('/index', methods=['GET','POST'])
@login.route('/', methods=['GET','POST'])
def auth():
    if request.method == "POST":
         email = request.form['email']
         senha = request.form['senha']

         user = People.query.filter_by(email=email.lower()).first()

        
         if user and user.senha == senha:
            return "<h1>Usuario Autenticado.</h1>"
         else:    
            return "<h1>Usuario ou senha errado.</h1>"
    elif request.method == "GET":
        return render_template('login/index.html')    
