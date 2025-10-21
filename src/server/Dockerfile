FROM python:3-alpine

WORKDIR /app

COPY . .

RUN pip install Flask

RUN pip install flask-socketio

CMD python app.py # flask --app app run --debug
