FROM python:3-alpine

ENV GEMINI_API_KEY=

WORKDIR /app

COPY . .

RUN pip install Flask

RUN pip install flask-socketio

# RUN pip install google-generativeai

RUN pip install -U google-genai

CMD flask --app app run --debug --host 0.0.0.0
