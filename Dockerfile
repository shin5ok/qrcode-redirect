FROM python:3.11-slim

COPY *.py pyproject.toml templates/ /

RUN pip install poetry && poetry install

CMD poetry run gunicorn main:app -b 0.0.0.0:8080
