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

  Explicando a lógica que utilizei para desenvolver esse módulo. Temos um método chamado `create()`, esse método pode receber os protocolos `POST` e `GET`.

  Se a requisição for `GET`, o formulário é renderizado. 
  
  Se a requisição for `POST`, os dados de `email` e `senha` são extraidos do formulário, um novo objeto do tipo `People` é instânciada com os dados `user = People(email,senha`. E o comando `user.add(user)` faz o registro no banco de dados.

  As linhas de código estão comentados para facilitar a compreensão.

  ```python
     # Importa as libs necessarias do Flask
     from flask import render_template,  Blueprint, request
     # Importa a class People para manipular os usuarios
     from app.model  import People

     # Definir o blueprint com o nome do módulo
     cadastro = Blueprint('cadastro',__name__)
     
     # Define a roda dentro do blueprint, por exemplo cadastro/ ou cadastro/index
     # Perceba que as duas rotas estao definidas
     @cadastro.route('/index', methods=['GET','POST'])
     @cadastro.route('/', methods=['GET','POST'])

     # Metodo que vai realizar as tarefas necessárias para criar o usuário
     def create():
         # Verifica se o request eh POST
         if request.method == "POST":
              # Obtem os valores dos formulários e salva na variavel email/senha
              email = request.form['email']
              senha = request.form['senha']
     
              # Instancia o objeto People com os valores email e senha
              user = People(email,senha)
              # Salvando o usuario
              if user.add(user):
                 # Se retornou True, é porque salvo 
                 return "<center><h1><em>Registro realizado com sucesso!!!</em></h1></center>"
              else:    
                 # Pode retornar um False
                 return "<center><h1><em>Falha ao criar a sua conta, tentnovamente!!!</em></h1></center>"
         # Verifica se o método é GET        
         elif request.method == "GET":
              # Renderiza o formulário         
              return render_template('cadastro/index.html')    
  ```

   A chamada `render_template`, basicamente renderiza o template que foi definido. O nosso template [`app/templates/cadastro/index.html`](ep4/app/templates/cadastro/index.html) é um html com um formulário.

   Segue o formulário em html básico.
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

- **Login**:

  Agora que já temos um usuário cadastrado, vamos criar a tela para o lógin do usuário. Portanto basicamente vamos verificar se a senha que o usuário digitou é a mesma que está gravado no banco de dados.

  No arquivo [`app/login/__init__.py`](ep4/login/__init__.py) temos toda a lógica necessária para fazer o login. Seguimos a mesma lógica do registro do usuário.

  O método `auth()` pode receber requisição `GET` e `POST`. Quando chegar uma requisição no protocolo `GET`, o formulário de autenticação é renderizada.

  Quando chegar uma requisição no método `POST`, os dados de email e login são extraidos do formulário enviado. 

  O primeiro processo de autenticação é localizar se o usuário existe no banco de dados.

  ```
  user = People.query.filter_by(email=email.lower()).first()
  ```

  Se o usuário existir, o cadastro do usuário será carregado e agora podemos comparar a senha.

  ```
  if user and user.senha == senha: 
  ```

  Para melhorar a compreensão do módulo, segue o módulo comentado.

  ```python
   
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
  ```
