
Agora a nossa aplicação já tem uma interface web para a criação do banco de dados. E como definido no arquivo de `config.py` a porta da aplicação é 8080. Portanto ao executar o docker, precisamos externalizar essa porta.

Para externalizar a porta 8080, utilizamos o parâmetro `-p`. 

```bash
$ docker run -it -p 8080:8080 apptask
```

Agora dentro do containner vamos inicializar aplicação e acompanhar o logs.

```bash
python run.py 
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 236-035-556
```

Na tela1, é solicitado o token definido no arquivo no arquivo `config.py` na variável `create_db_token`. Futuramente vamos melhorar esse método de geração de token.

![form](lab2-img1.png)

E na tela2, temos o banco de dados criado.

![create_database](lab2-img2.png)


Dessa forma finalizamos o laboratório 2.