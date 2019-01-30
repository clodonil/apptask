from flask import render_template,  Blueprint, request
from app.model  import People



cadastro = Blueprint('cadastro',__name__)


@cadastro.route('/index', methods=['GET','POST'])
@cadastro.route('/', methods=['GET','POST'])
def create_people():
    if request.method == "POST":
         email = request.form['email']
         senha = request.form['senha']

         user = People(email,senha)
         if user.add(user):
            return "<h1>Usuario criado com sucesso.</h1>"
         else:    
            return "<h1>falha ao criar usuario.</h1>"
    elif request.method == "GET":
        return render_template('cadastro/index.html')    

