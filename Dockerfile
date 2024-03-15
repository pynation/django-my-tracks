FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y

RUN mkdir -p /usr/src

COPY poetry.lock pyproject.toml /usr/src/

WORKDIR /usr/src/
RUN pip install -U pip
RUN pip install poetry==1.8.2

RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

COPY . /usr/src

RUN chmod +x /usr/src/scripts/*

ENTRYPOINT [ "/usr/src/scripts/entrypoint.sh" ]