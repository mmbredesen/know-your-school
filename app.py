from flask import Flask, render_template
from algoliasearch import algoliasearch
import json, urllib2

app = Flask(__name__)

client = algoliasearch.Client('E3Z5BWU5LE', 'f6f8da14853c3bdfa71fa1491c4ca78e')
index = client.init_index('know-your-school')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data")
def data():
    return render_template("data.html")

@app.route("/school_safety", methods=["GET","POST"])
def school_safety():
    return render_template("school_safety.html")

@app.route("/petitions")
def petitions():
    return render_template("petitions.html")

if __name__ == "__main__":
    app.run()