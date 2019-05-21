FROM python:alpine3.7

ADD owm.py /

ADD variable.txt /

RUN pip install -r requirements.txt

CMD [ "python", "./owm.py" ]