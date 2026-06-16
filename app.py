from flask import Flask, render_template, jsonify, request
from src.helper import rag_chain
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    print(msg)
    response = rag_chain.invoke(msg)
    print("Response : ", response)
    return str(response)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)