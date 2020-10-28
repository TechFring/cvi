from app import app, login_manager, db
from flask_login import login_user, logout_user, current_user
from flask import render_template, request, redirect, url_for, flash

# Models
from app.models.secretaria import Secretaria


# Rotas
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        if current_user.is_authenticated:
            return redirect(url_for("corretores"))

        return render_template("login.html")

    nome_usuario = request.form.get("nome_usuario")
    senha = request.form.get("senha")

    secretaria = Secretaria.query.filter_by(nome_usuario=nome_usuario).first()

    if not secretaria or not secretaria.verificar_senha(senha):
        flash("Credenciais incorretas")
        return redirect(url_for("login"))

    login_user(secretaria)
    return redirect(url_for("corretores"))


# Descomente para inserir secretária
# @app.route("/login/criar-usuario", methods=["GET"])
# def criar_usuario():
#     nome = "Secretária"
#     nome_usuario = "secretaria"
#     senha = "12345"

#     secretaria = Secretaria(nome, nome_usuario, senha)
#     db.session.add(secretaria)
#     db.session.commit()

#     return redirect(url_for("login"))


@app.route("/logout", methods=["GET"])
def logout():
    logout_user()
    return redirect(url_for("login"))