FROM ubuntu:latest
LABEL maintainer Clodonil Trigo "clodonil@nisled.org"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /apptask
WORKDIR /apptask
RUN pip install -r requirements
#ENTRYPOINT ["python"]
#CMD ["run.py"]


