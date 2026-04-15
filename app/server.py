from flask import Flask, request, jsonify, send_from_directory
from app.agents.baseline_agent import agent
import os

app = Flask(
    __name__,
    static_folder="./static",
    static_url_path=""
)

@app.route("/")
def home():
    return send_from_directory("static", "index.html")

@app.route("/api/test", methods=["POST"])
def test_endpoint():
    # Your endpoint logic
    return jsonify({"status": "ok"})