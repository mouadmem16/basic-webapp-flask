import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    hostname = os.environ["NAME"]
    return "<h1>Welcome!</h1> </br> <h2>This is the node " + hostname + "</h2>"

@app.route('/how are you')
def hello():
    return 'I am good, how about you?'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
