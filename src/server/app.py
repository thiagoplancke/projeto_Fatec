from flask import Flask, render_template
from flask_socketio import SocketIO

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
    print('received message: ' + str(data))

@socketio.on('json')
def handle_json(json):
    print('received json: ' + str(json))

if __name__ == '__main__':
    socketio.run(app)
