from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data")
def data():
    return render_template("data.html")

@app.route("/petitions")
def petitions():
    return render_template("petitions.html")

if __name__ == "__main__":
    app.run()