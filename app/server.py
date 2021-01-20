
from flask import Flask, render_template
import socket

app = Flask(__name__)


@app.route("/")
def hello():
    return f"Hello World"


@app.route("/ping")
def ping():
    return f"pong"


@app.route("/anant")
def tyagi():
    return render_template('anant.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("8080"), debug=True)
