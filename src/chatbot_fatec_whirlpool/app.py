from flask import Flask, render_template, request, jsonify
from port_ia import responder_ia  # <-- import da outra pasta com a "IA"

app = Flask(__name__)

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
