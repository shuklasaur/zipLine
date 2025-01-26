import glob
import os
import hashlib
import pandas as pd

import flask 

app = flask.Flask(__name__)


@app.route("/")
def index():
    return flask.redirect("/welcome")


@app.route("/welcome")
def welcome():
    # TODO: create welcome screen
    return "Hello, From the children of Planet Earth"


@app.route("/welcome/login")
def login():
    # TODO: create login screen
    return "login screen"


@app.route("/welcome/signup")
def signup():
    # TODO: create signup screen
    return "signup screen."

@app.route("/post/image",methods=["POST"])
def postimage():

    print(flask.request.files.get("image"))
    flask.request.files.get("image").save(f"testData/new-{flask.request.files.get('image').filename}")

    return 'GOOD'