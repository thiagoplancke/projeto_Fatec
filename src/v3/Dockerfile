FROM python:3-alpine

WORKDIR /app

COPY . .

RUN pip install Flask

RUN pip install flask-socketio

RUN pip install google-generativeai

CMD flask --app app run --debug --host 0.0.0.0
