from flask import Flask, render_template, request, jsonify
import json
import datetime
from port_ia import responder_ia  # <-- import da outra pasta com a "IA"

app = Flask(__name__)

@app.route("/feedback", methods=["POST"])
def feedback():
    data = request.get_json()
    user_message = data.get("user_message")
    feedback_type = data.get("feedback_type")
    bot_message = data.get("bot_message")
    timestamp = data.get("timestamp", datetime.datetime.now().isoformat())
    with open("feedback_log.json", "a", encoding="utf-8") as f:
        json.dump({
            "feedback_type": feedback_type,
            "user_message": user_message,
            "bot_message": bot_message,
            "timestamp": timestamp
        }, f, ensure_ascii=False)
        f.write("\n")
    return jsonify({"status": "ok", "message": "Feedback recebido"})

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    data = request.get_json()
    mensagem_usuario = data.get("message", "")

    # Resposta gerada pela IA Python
    resposta = responder_ia(mensagem_usuario)

    return jsonify({"response": resposta})

if __name__ == "__main__":
    app.run(debug=True)
