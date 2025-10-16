FROM python:alpine

WORKDIR /app

COPY src/chatbot/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src/chatbot/ .

CMD ["python", "chatbot.py"]
