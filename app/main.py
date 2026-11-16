
from flask import Flask, jsonify
from datetime import datetime, timezone

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to My DevOps Project!",
        "application": "DevOps REST API",
        "version": "1.0.0",
        "status": "running"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat()
    })

@app.route("/api/status")
def status():
    return jsonify({
        "application": "DevOps REST API",
        "status": "operational"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
