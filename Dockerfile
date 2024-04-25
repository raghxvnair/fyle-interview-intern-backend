FROM python:3.8-slim

ENV FLASK_APP=core/server.py
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y \
    bash \
 && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

RUN rm core/store.sqlite3
RUN flask db upgrade -d core/migrations/

EXPOSE 7755

CMD [ "bash", "run.sh" ]