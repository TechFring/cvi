from app import app, db
from flask_login import current_user
from flask import render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash

# Models
from app.models.secretaria import Secretaria


@app.route("/configuracoes", methods=["GET", "POST"])
def configuracoes():
    if not current_user.is_authenticated:
        return redirect(url_for("login"))

    secretaria = Secretaria.query.filter_by(id=session["_user_id"]).first()

    if request.method == "GET":
        return render_template("configuracoes.html", secretaria=secretaria)

    # Editando dados da conta
    senha = request.form["senha"]
    secretaria.nome = request.form["nome"]
    secretaria.nome_usuario = request.form["nome_usuario"]
    secretaria.email = request.form["email"]

    if senha != "":
        secretaria.senha = generate_password_hash(senha)

    db.session.commit()

    return render_template("configuracoes.html", secretaria=secretaria)
