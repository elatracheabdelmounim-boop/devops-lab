from flask import Flask
app = Flask(__name__)

@app.route("/")
def hi():
    return "Hello DevOps!"

app.run(host="0.0.0.0", port=5000)
