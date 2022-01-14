import os
from flask import Flask, render_template, request

# Configure application
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", name=request.args.get("name", "world"))

@app.route("/greet")
def greet():
    return render_template("greet.html", name=request.args.get("name", "world"))