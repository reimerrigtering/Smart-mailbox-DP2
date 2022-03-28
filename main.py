from flask import Flask

app = Flask(__name__)

@app.route("/")
def serve_home():
    return "hallo test"

app.run("0.0.0.0")
