import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome to the Agile Lab! This is tanaya here"

@app.route('/whats new?')
def hello():
    return 'learning docker!!!!!'

if __name__ == "__main__":
    app.run()
