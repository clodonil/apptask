# 5. Episódio - Template

No episódio anterior criamos a tela de cadastro de usuário e a tela de login. Mas para continuarmos a desenvolver a nossa aplicação, é melhor dar uma cara/personalidade para ela.

Sempre desenvolva com um layout, fica bem mais simples e estruturado. Portanto nesse episódio vamos ver como criar um template básico.

O flask suporte a estrutura de template em [Jinja2](http://jinja.pocoo.org/docs/2.10/), vale a pena dar uma olhada no manual para conhecer os outros recursos que não serão tratados nesse documento.

> A formatação de html vamos utilizar o [Materialize](https://materializecss.com/), não vamos entrar nesse detalhe, acredito que o seu designer vai ficar bem melhor que o meu.







```html
<html>
    <head>
        <title> {{ title }}</title>
    </head>
  <body>
     <h1> AppTask </h1> 
    {% block content %}{% endblock %}
  </body>
</html>
```

```html
{% extends "layout.html" %}
{% block content %}
    <div class="row">
	     <div class="col s12">
            <h1 class="header center orange-text" class="center-align">Setup da Aplicação</h1>
            <div class="center-align">Criação do Banco de Dados</div>
            <div class="center-align"><p><em>Para criação do banco de dados digite o token definido na configuração da aplicação.</em></p></div>
         </div>
	 <div class="row" class="center-align">
         <form action="" method="post" class="col s12">
		    <div class="row">
	            <div class="input-field col s12">
                    <input placeholder="token no arquivo config.py" id="token" type="text" class="validate">
                     <label for="token">Digite o token</label>
                </div>
            </div>   
            <div class="row">
	           <div class="input-field col s12">
                   <input type="submit" class="waves-effect waves-light btn">
               </div>
            </div>   
        </form>
	  </div>
	</div>
{% endblock %}
```
Lembre-se de realiar o build para essa nova imagem:

```bash
$ docker build -t apptask:ep5 .
```

Para externalizar a porta 8080, utilizamos o parâmetro `-p`. 

```bash
$ docker run -it -p 8080:8080 apptask:ep5
