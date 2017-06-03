FROM python:latest
ADD . /opt/todo
WORKDIR /opt/todo
RUN pip install -r requirements.txt
