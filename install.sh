#!/usr/bin/env bash

cat > dockerfile << EOF
FROM python:alpine3.7

ADD owm.py /

RUN pip install -r requirements.txt

CMD [ "python", "./owm.py", "$1", "$2" ]
EOF

docker build -t python-owm

docker run python-owm