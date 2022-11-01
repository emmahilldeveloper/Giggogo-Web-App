import json

from flask import Flask, redirect, render_template, session
from jinja2 import StrictUndefined

app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

@app.route("/")
def index():
    """Returns the homepage."""
    return render_template("homepage.html")

@app.route("/signup")
def sign_up():
    """Shows sign up form to create a new user."""

    return render_template("signup.html")

@app.route("/login")
def login():
    """Allows established users to log into their accounts."""

    return render_template("login.html")
# @app.route("/profile")
# def profile():


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        use_reloader=True,
        use_debugger=True,
    )