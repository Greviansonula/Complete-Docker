from flask import Flask
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Hellow world from dockers"

if __name__ == "__main__":
    app.run(debug=True)