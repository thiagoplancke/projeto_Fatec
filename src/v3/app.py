from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
import google.generativeai as genai

import os

GEMINI_API_KEY=os.getenv("GEMINI_API_KEY", "none")

print(f"GEMINI_API_KEY: {GEMINI_API_KEY}")

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel('gemini-2.5-flash')

app = Flask(__name__, static_folder='static', static_url_path='/static') 

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat/<chatid>')
def show_chat(chatid):
    return render_template('chat.html', chatid=chatid)

socketio = SocketIO()

socketio.init_app(app)

@socketio.on('message')
def handle_message(data):
    question = data['message']
    chat_id = data['chatId']

    response = model.generate_content(str(question))

    answer = str(response.text)

    emit('message', { 'chatId': str(chat_id), 'message': str(answer)})

@socketio.on('json')
def handle_json(json):
    emit('json', json)

if __name__ == '__main__':
    socketio.run(app, allow_unsafe_werkzeug=True)
