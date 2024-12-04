FROM python:3
ARG BASE 

RUN apt-get update
RUN apt-get -y install locales less && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8 
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

WORKDIR ${BASE} 
COPY pyproject.toml poetry.lock README.md ${BASE}/
COPY mailer/ ${BASE}/mailer/
COPY web/ ${BASE}/web/
#
RUN pip install --upgrade pip poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
