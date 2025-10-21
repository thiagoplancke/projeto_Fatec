FROM python:3-alpine

WORKDIR /app

COPY . .

RUN pip install Flask

RUN pip install flask-socketio

RUN pip install google-generativeai

CMD python app.py # flask --app app run --debug
