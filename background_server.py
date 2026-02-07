from flask import Flask, request, jsonify
from flask_cors import CORS

from agents.text_agent import analyze_text
from agents.url_agent import analyze_url
from agents.sender_agent import analyze_sender


app = Flask(__name__)
CORS(app)   # <-- IMPORTANT


@app.route("/scan", methods=["POST"])
def scan():

    data = request.json

    url = data.get("url", "")
    text = data.get("text", "")

    url_risk = analyze_url(url)
    text_risk = analyze_text(text) if text else 0
    sender_risk = analyze_sender(text) if text else 0

    final = (url_risk + text_risk + sender_risk) / 3

    print("DEBUG:", url_risk, text_risk, sender_risk, "=>", final)

    if final >= 0.45:
        decision = "PHISHING"
    elif final >= 0.25:
        decision = "WARNING"
    else:
        decision = "SAFE"


    return jsonify({
        "decision": decision,
        "score": round(final, 3)
    })


if __name__ == "__main__":

    print("PhishGuard Background Service Running...")
    app.run(host="127.0.0.1", port=5050)
