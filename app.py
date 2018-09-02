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

@app.route("/school_safety/manhattan", methods=["GET","POST"])
def manhattan_safety():
    return render_template("manhattan_safety.html")

@app.route("/school_safety/brooklyn", methods=["GET","POST"])
def brooklyn_safety():
    return render_template("brooklyn_safety.html")

@app.route("/school_safety/bronx", methods=["GET","POST"])
def bronx_safety():
    return render_template("bronx_safety.html")

@app.route("/school_safety/queens", methods=["GET","POST"])
def queens_safety():
    return render_template("queens_safety.html")

@app.route("/school_safety/staten", methods=["GET","POST"])
def staten_safety():
    return render_template("staten_safety.html")

@app.route("/vadir", methods=["GET","POST"])
def vadir():
    return render_template("vadir.html")

@app.route("/lead", methods=["GET","POST"])
def lead():
    return render_template("lead.html")

@app.route("/contact", methods=["GET","POST"])
def contact():
    return render_template("Contact.html")

@app.route("/support", methods=["GET","POST"])
def support():
    return render_template("Support.html")

if __name__ == "__main__":
    app.run()