from application import app, db
from flask import redirect, render_template, request, url_for
from application.tasks.models import Task



@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", tasks = Task.query.all())