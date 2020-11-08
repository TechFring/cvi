from app import app, db
from flask_login import current_user
from flask import render_template, request, redirect, url_for
import datetime

# Models
from app.models.visita import Visita
from app.models.imovel import Imovel
from app.models.corretor import Corretor


# Rotas
@app.route("/visitas", methods=["GET"])
def visitas():
    if not current_user.is_authenticated:
        return redirect(url_for("login"))

    visitas = Visita.query.all()

    for v in visitas:
        imovel = Imovel.query.filter_by(id=v.id_imovel).first()
        corretor = Corretor.query.filter_by(id=v.id_corretor).first()

        dia = datetime.datetime.strptime(str(v.dia), "%Y-%m-%d %H:%M:%S")
        dia_formatado = datetime.datetime.strftime(dia, "%d/%m/%Y %H:%M")

        v.dia_formatado = dia_formatado

        v.capa = imovel.capa
        v.nome_corretor = corretor.nome

    return render_template("visitas.html", visitas=visitas)


@app.route("/visitas/cadastrar", methods=["GET", "POST"])
def cadastrar_visita():
    if not current_user.is_authenticated:
        return redirect(url_for("login"))

    if request.method == "GET":
        imoveis = Imovel.query.all()
        corretores = Corretor.query.all()
        return render_template("cadastrar-visita.html", visita=None, imoveis=imoveis, corretores=corretores)

    # Cadastrando visita
    id_imovel = request.form['id_imovel']
    id_corretor = request.form['id_corretor']
    dia = request.form['dia']
    nome_cliente = request.form['nome_cliente']
    telefone_cliente = request.form['telefone_cliente']

    visita = Visita(id_imovel, id_corretor, dia,
                    nome_cliente, telefone_cliente, capa=None, nome_corretor=None, dia_formatado=None)
    db.session.add(visita)
    db.session.commit()

    return redirect(url_for("visitas"))


@app.route("/visitas/editar/<id>", methods=["GET", "POST"])
def editar_visita(id):
    if not current_user.is_authenticated:
        return redirect(url_for("login"))

    # recupera os dados da visita
    visita = Visita.query.filter_by(id=id).first()

    if not visita:
        return redirect(url_for("visitas"))

    if request.method == "GET":
        imoveis = Imovel.query.all()
        corretores = Corretor.query.all()
        return render_template("cadastrar-visita.html", visita=visita, imoveis=imoveis, corretores=corretores)

    # Editando visita
    visita.id_imovel = request.form['id_imovel']
    visita.id_corretor = request.form['id_corretor']
    visita.dia = request.form['dia']
    visita.nome_cliente = request.form['nome_cliente']
    visita.telefone_cliente = request.form['telefone_cliente']

    db.session.commit()

    return redirect(url_for("visitas"))


@app.route("/visitas/apagar/<id>", methods=["GET"])
def apagar_visita(id):
    if not current_user.is_authenticated:
        return redirect(url_for("login"))

    # recupera os dados da visita
    visita = Visita.query.filter_by(id=id).first()

    if not visita:
        return redirect(url_for("visitas"))

    # Apagando visita
    db.session.delete(visita)
    db.session.commit()

    return redirect(url_for("visitas"))
