from app import app, db
from flask_login import current_user
from flask import render_template, request, redirect, url_for

# Models
from app.models.corretor import Corretor


# Rotas
@app.route("/corretores", methods=["GET"])
def corretores():
    if not current_user.is_authenticated:
        return redirect(url_for("login"))

    corretores = Corretor.query.all()

    return render_template("corretores.html", corretores=corretores)


@app.route("/corretores/cadastrar", methods=["GET", "POST"])
def cadastrar_corretor():
    if not current_user.is_authenticated:
        return redirect(url_for("login"))

    if request.method == "GET":
        return render_template("cadastrar-corretor.html", corretor=None)

    # Cadastrando corretor
    creci = request.form['creci']
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']

    corretor = Corretor(creci, nome, email, senha)
    db.session.add(corretor)
    db.session.commit()

    return redirect(url_for("corretores"))


@app.route("/corretores/editar/<id>", methods=["GET", "POST"])
def editar_corretor(id):
    if not current_user.is_authenticated:
        return redirect(url_for("login"))

    # recupera os dados do corretor
    corretor = Corretor.query.filter_by(id=id).first()

    if not corretor:
        return redirect(url_for("corretores"))

    if request.method == "GET":
        return render_template("cadastrar-corretor.html", corretor=corretor)

    # Editando corretor
    corretor.creci = request.form['creci']
    corretor.nome = request.form['nome']
    corretor.email = request.form['email']
    corretor.senha = request.form['senha']

    db.session.commit()

    return redirect(url_for("corretores"))


@app.route("/corretores/apagar/<id>", methods=["GET"])
def apagar_corretor(id):
    if not current_user.is_authenticated:
        return redirect(url_for("login"))

    # recupera os dados do corretor
    corretor = Corretor.query.filter_by(id=id).first()

    if not corretor:
        return redirect(url_for("corretores"))

    # Apagando corretor
    db.session.delete(corretor)
    db.session.commit()

    return redirect(url_for("corretores"))
