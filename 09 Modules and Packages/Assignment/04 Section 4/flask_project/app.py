from flask import Flask
import requests
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello from Flask!"

if __name__ == "__main__":
    app.run(debug=True)
