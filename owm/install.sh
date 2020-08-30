#!/usr/bin/env bash

cat > Dockerfile << EOF
FROM python:alpine3.7

COPY owm.py .

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD [ "python", "./owm.py", "$1", "$2" ]
EOF

docker build -t python-owm

docker run python-owm
