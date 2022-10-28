import json

from flask import Flask, redirect, render_template, session, url_for
from jinja2 import StrictUndefined

app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

@app.route("/")
def index():
    """Returns the homepage."""

    return render_template("homepage.html")

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        use_reloader=True,
        use_debugger=True,
    )