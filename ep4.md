# 4. Episódio - Registro de Usuário e Login

No episódio anterior criamos o banco de dados através de uma interface WEB, no primeiro acesso.

Nesse episódio vamos avançar os nossos conhecimentos, permitido o registro de novos usuários na base de dados e também criando uma tela de login para aplicação.

> Nesse momento não estamos preocupados em criar links, interligados as páginas, veremos isso no próximo episódio.

Como vamos criar a tela de login e a tela de cadastro de novos usuários, vamos chamar essas telas de módulos.

Vimos em episódios anteriores, cada módulo é um diretório criado na pasta `app` e como a tela de lógin e de cadastro terá um formulário, precisamos criar a mesma estrutura dentro da pasta `templates` para o módulo encontrar os arquivos `html`.

Portanto vamos começar criando a estrutura dos módulos.

```bash
 $ mkdir app/{login,cadastro}
 $ touch app/{login,cadastro}/__init__.py
 $ mkdir app/templates/{login,cadastro}
```

Os vários módulos do nosso projeto serão orquestrado pela lib `blueprint` que simplifica bastante essa etapa.

A cada novo módulo, precisamos editar o arquivo [`app/__init__.py`](ep4/app/__init__.py) para adicionar no projeto.

Basicamente precisamos importar a `class` do módulo e definir a rota que o módulo vai trabalhar. Não adicionei o arquivo inteiro, apenas as linhas necessárias para o compreensão. 

[`app/__init__.py`](ep4/app/__init__.py) 

```python
...
...
# Modulos
from app import model
# Importar o módulo cadastro
from app.cadastro import cadastro
# Importar o módulo login
from app.login    import login

# Definir a rota para o modulo cadastro
app.register_blueprint(cadastro, url_prefix='/cadastro')
# Definir a rota para o modulo login
app.register_blueprint(login,    url_prefix='/login'   )
```

Com os módulos apontados no arquivo [`app/__init__.py`](ep4/app/__init__.py), vamos construir os módulo de cadastro e login. Vamos começar pelo cadastro.

- **Cadastro**:

  A ideia desse módulo é cadastrar/registrar um novo usuário.

  Vamos começar criando a lógica do módulo no arquivo [`app/cadastro/__init__.py`](ep4/app/cadastro/__init__.py)


  ```python
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
                 return "<center><h1><em>Falha ao criar a sua conta, tentnovamente!!!</em></h1></center>"
         elif request.method == "GET":     
                  return render_template('cadastro/index.html')    
  ```

   A chamada `render_template`, basicamente renderiza o template que foi definido. O nosso template [`cadastro/index.html`](ep4/app/templates/cadastro/index.html) é um html com um formulário.

   ```html
   <html>
       <title>Criação de Usuário</title>
       <body>
           <center>
           <h1> Criação de uma nova conta</h1>
           <p><em>Preeencha o formulário para criação de um novo usuário.</em></p>
           <span>
               <form action="" method="post">
                    <span>
                      <label> E-Mail: </label>
                      <br>
                      <input type="text" name="email">
                    </span>
                    <br>
                   <span>
                      <label> Senha: </label>
                      <br>
                      <input type="password" name="senha">
                   </span>
                   <br>
                   <span>   
                      <label> Confirme Senha: </label>
                      <br>
                      <input type="password" name="confirm_senha">
                   </span> 
                   <br><br>
   		       <input type="submit" value="Criar Conta">
               </form>
           </span>
           </center>
       </body>
   </html>
   ```    
# Criar a tela de Cadastro


# Criar a tela de Login


# Ajustar o campo `senha` do Banco de Dados e Email para lower().


# Templates em HTML 