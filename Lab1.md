
Com o `Dockerfile` criado, podemos agora construir a imagem docker e assim poder validar o que fizemos até aqui.

Realizando o build da image apptask:latest:

```bash
$ docker build -t apptask:latest .
```

Vamos rodar a imagem e realizar algumas testes em nossa aplicação: 

```bash
$ docker run -it apptask
```

Quando executamos a imagem, entramos na linha de comando do python, representando pelo ">>>". Como nossa aplicação não está pronta ainda, vamos testar dessa forma:

Primeiramente vamos importa as bibliotecas da nossa aplicação:

Vamos importar a função `db` que está dentro do arquivo `__init__.pp` dentro da pasta `app`. É necessário importar para poder criar o banco de dados.

```python
>>> from app import db
>>> db.create_all()
```

Agora vamos importar a lib `datetime` para obter a data atual e também vamos importar do arquivo da pasta `app/model/__init__.py` para manipular as tabelas do banco de dados.

```python
>>> import datetime
>>> from app.model import People, Task
```
Com as classes das tabela importadas, vamos criar os registros da tabela `People` e `Task`.

```python
>>> user = People('user1@localhost','x')
>>> user.add(user)

>>> t1 = Task('Atividade 1',now,user.id)
>>> now = datetime.datetime.now()
>>> t1 = Task('Atividade 1',now,user.id)
>>> t1.add(t1)
```

Agora que temos os registros criados, vamos verificar o relacionamento entre as tabelas:

```python
>>> t1.people
<People u'user1@localhost'>
>>> user = People.query.get(1)
>>> user.tasks
[<Task u'Atividade 1'>]
```

Dessa forma finalizamos o laboratório 1.