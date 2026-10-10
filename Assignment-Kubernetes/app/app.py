from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Student Academic Platform running on Kubernetes!",
        "application": "Student Academic Platform",
        "hostname": socket.gethostname(),
        "version": "1.0.0"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/students")
def students():
    return jsonify({
        "students": [
            {"id": 1, "name": "Student One", "course": "CSE AIML"},
            {"id": 2, "name": "Student Two", "course": "CSE AIML"}
        ]
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
