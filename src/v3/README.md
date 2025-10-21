# Server Fatec Whirlpool

## Python libraries

[Gemini API](https://ai.google.dev/gemini-api/docs/migrate?hl=pt-br)

[Google AI Studio - API Keys](https://aistudio.google.com/api-keys)

[Flask-SocketIO](https://flask-socketio.readthedocs.io/en/latest/index.html)

[Flask](https://flask.palletsprojects.com/en/stable/quickstart/#)

## How to run in Python

Install [Python](https://www.python.org/downloads/)

In ./src/v3, run in Python:

```bash
python app.py 
```

Open `http://127.0.0.1:5000`

## How to run in Docker

Install [Docker](https://www.docker.com/)

```bash
docker compose build server 
```

```bash
docker run --network host tarsislimafatec/server_fatec_whirlpool:latest 
```

## TODOs

- [ ] Train Gemini with Whirpool questions

- [ ] Fix Gemini answer on browser (HTML instead Markdown)

- [ ] Set Chat ID on Gemii answers
