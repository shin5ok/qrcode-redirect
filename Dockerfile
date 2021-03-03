FROM python:3.8-slim
LABEL MAINTAINER kawanos@google.com

COPY . .

RUN python -m pip install -r requirements.txt

CMD exec gunicorn main:app -b 0.0.0.0:8080