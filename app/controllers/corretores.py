from app import app, db
from flask_login import current_user
from flask import render_template, request, redirect, url_for

# Models
from app.models.corretor import Corretor


# Rotas
@app.route("/corretores", methods=["GET", "POST"])
def corretores():
    if not current_user.is_authenticated:
        return redirect(url_for("login"))

    corretores = Corretor.query.all()

    return render_template("corretores.html", corretores=corretores)


# Rotas
@app.route("/corretores/cadastrar", methods=["GET", "POST"])
def cadastrar_corretor():
    if not current_user.is_authenticated:
        return redirect(url_for("login"))

    if request.method == "GET":
        return render_template("cadastrar-corretor.html")

    # Cadastrando corretor
    creci = request.form['creci']
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']

    corretor = Corretor(creci, nome, email, senha)
    db.session.add(corretor)
    db.session.commit()

    return redirect(url_for("corretores"))
