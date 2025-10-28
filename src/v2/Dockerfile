FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt && \
    python -m spacy download pt_core_news_lg

COPY . .

EXPOSE 7860

CMD ["python", "chat4.py"]
