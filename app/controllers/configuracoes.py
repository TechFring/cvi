from app import app, db
from flask_login import current_user
from flask import render_template, request, redirect, url_for, session

# Models
from app.models.secretaria import Secretaria

@app.route("/configuracoes", methods=["GET", "POST"])
def configuracoes():
    if not current_user.is_authenticated:
        return redirect(url_for("login"))

    print(current_user)

    return render_template("configuracoes.html")