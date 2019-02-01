# Episódio 1 - Visão geral do projeto

Vamos começar a nossa jornada com aplicação que será utilizada como base. Vamos desenvolver um aplicativo bem simples que registra as tarefas que devem ser executadas por uma pessoa.

O nome da nossa aplicação é `apptask`

A prototipação da aplicação é essa:


![tela_inicial](img/ep1-img1.png)


Vamos utilizar as seguintes tecnologias para o desenvolvimento:

- Python
- Flash

Aplicação vai rodar em um containner Docker. Portanto vamos utilizar o seguinte `Dockerfile` durante o projeto.

```
FROM ubuntu:latest
LABEL maintainer Clodonil Trigo "clodonil@nisled.org"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /apptask
WORKDIR /apptask
RUN pip install -r requirements
ENTRYPOINT ["python"]
CMD ["run.py"]
```

