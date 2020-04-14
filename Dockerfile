FROM python:3

ADD . /hermes

WORKDIR /hermes

RUN pip install -r requirements.txt

CMD python backend/manage.py runserver 0.0.0.0:8000

