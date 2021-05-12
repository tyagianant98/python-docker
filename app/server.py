
from flask import Flask, render_template
import socket

app = Flask(__name__)


@app.route("/")
def hello():
    machine = socket.gethostname()
    return f"Hello World from container {machine}"


@app.route("/ping")
def ping():
    return f"pong"


@app.route("/ngbps")
def ndv():
    return f"This is a Data Center in Bhiwadi,Rajisthan"



@app.route("/anant")
def tyagi():
    return render_template('anant.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("8080"), debug=True)

