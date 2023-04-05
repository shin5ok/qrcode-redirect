FROM python:3.11-slim

COPY *.py pyproject.toml poetry.lock templates/ /

RUN pip install poetry
RUN poetry config virtualenvs.create false --local && poetry install

ENTRYPOINT ["/bin/bash", "-c", "poetry run gunicorn main:app -b 0.0.0.0:${PORT}"]
# CMD poetry run python main.py
