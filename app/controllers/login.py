from app import app, login_manager, db, mail
from flask_login import login_user, logout_user, current_user
from flask import render_template, request, redirect, url_for, flash
from flask_mail import Message
import uuid
from werkzeug.security import generate_password_hash

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
        flash("Credenciais incorretas", "danger")
        return redirect(url_for("login"))

    login_user(secretaria)
    return redirect(url_for("corretores"))


# Descomente para inserir secretária
# @app.route("/login/criar-usuario", methods=["GET"])
# def criar_usuario():
#     nome = "Secretária"
#     nome_usuario = "secretaria"
#     email = "seu_email@gmail.com"
#     senha = "12345"
#     token = str(uuid.uuid4().hex)

#     secretaria = Secretaria(nome, nome_usuario, email, senha, token)
#     db.session.add(secretaria)
#     db.session.commit()

#     return redirect(url_for("login"))


@app.route("/redefinir-senha", methods=["GET", "POST"])
def redefinir_senha():

    if request.method == "GET":
        if current_user.is_authenticated:
            return redirect(url_for("corretores"))

        return render_template("redefinir-senha.html")

    email = request.form["email"]

    secretaria = Secretaria.query.filter_by(email=email).first()

    if not secretaria:
        flash("Email não cadastrado na base de dados", "danger")
        return redirect("/redefinir-senha")

    token = uuid.uuid4().hex
    secretaria.token = token
    db.session.commit()

    msg = Message(
        "Redefinir senha",
        sender="cvisuporte9@gmail.com",
        recipients=[secretaria.email]
    )

    link = f"http://localhost:5000/alterar-senha/{token}"

    msg.html = render_template("email.html", link=link, usuario=secretaria.nome)

    mail.send(msg)
    flash("Foi enviada uma mensagem contendo instruções para a redefinição de sua senha", "success")
    return redirect("/redefinir-senha")


@app.route("/alterar-senha/<token>", methods=["GET", "POST"])
def alterar_senha(token):

    secretaria = Secretaria.query.filter_by(token=token).first()

    if not secretaria:
        return redirect("/login")

    if request.method == "GET":
        if current_user.is_authenticated:
            return redirect(url_for("corretores"))
            
        return render_template("alterar-senha.html")

    token = uuid.uuid4().hex
    senha = request.form["senha"]
    secretaria.token = token
    secretaria.senha = generate_password_hash(senha)
    db.session.commit()

    flash("Senha alterada com sucesso", "success")
    return redirect("/login")


@app.route("/logout", methods=["GET"])
def logout():
    logout_user()
    return redirect(url_for("login"))
