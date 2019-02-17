from flask import render_template,  Blueprint, request
from app.model  import People


cadastro = Blueprint('cadastro',__name__)

@cadastro.route('/index', methods=['GET','POST'])
@cadastro.route('/', methods=['GET','POST'])
def create():
    if request.method == "POST":
         email = request.form['email']
         senha = request.form['senha']

         user = People(email,senha)
         if user.add(user):
            return "<center><h1><em>Registro realizado com sucesso!!!</em></h1></center>"
         else:    
            return "<center><h1><em>Falha ao criar a sua conta, tente novamente!!!</em></h1></center>"
    elif request.method == "GET":
        return render_template('cadastro/index.html')    

