from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import requests
import json
import os
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app)

load_dotenv()

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the backend!"})

@app.route("/hotel-search")
def hotelSearch():
    return jsonify({"message": "Welcome to the backend!"})