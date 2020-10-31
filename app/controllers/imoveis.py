from app import app, db
from flask_login import current_user
from flask import render_template, request, redirect, url_for
import os

# Models
from app.models.imovel import Imovel


# Rotas
@app.route("/imoveis", methods=["GET"])
def imoveis():
    if not current_user.is_authenticated:
        return redirect(url_for("login"))

    refresh = request.args.get("refresh")
    imoveis = Imovel.query.all()

    return render_template("imoveis.html", imoveis=imoveis, refresh=refresh)


@app.route("/imoveis/cadastrar", methods=["GET", "POST"])
def cadastrar_imovel():
    if not current_user.is_authenticated:
        return redirect(url_for("login"))

    if request.method == "GET":
        return render_template("cadastrar-imovel.html", imovel=None)

    # Cadastrando imóvel
    endereco = request.form['endereco']
    latitude = request.form['latitude']
    longitude = request.form['longitude']
    tamanho = request.form['tamanho']
    quartos = request.form['quartos']
    banheiros = request.form['banheiros']
    garagem = request.form['garagem']
    descricao = request.form['descricao']

    imovel = Imovel(endereco, latitude, longitude, tamanho, quartos,
                    banheiros, garagem, descricao, doc_imovel=None, doc_proprietario=None, capa=None)

    db.session.add(imovel)
    db.session.commit()

    return redirect(url_for("imoveis"))


@app.route("/imoveis/editar/<id>", methods=["GET", "POST"])
def editar_imovel(id):
    if not current_user.is_authenticated:
        return redirect(url_for("login"))
    
    # recupera os dados do imóvel
    imovel = Imovel.query.filter_by(id=id).first()

    if not imovel:
        return redirect(url_for("imoveis"))

    if request.method == "GET":
        return render_template("cadastrar-imovel.html", imovel=imovel)

    # Editando imóvel
    imovel.endereco = request.form['endereco']
    imovel.latitude = request.form['latitude']
    imovel.longitude = request.form['longitude']
    imovel.tamanho = request.form['tamanho']
    imovel.quartos = request.form['quartos']
    imovel.banheiros = request.form['banheiros']
    imovel.garagem = request.form['garagem']
    imovel.descricao = request.form['descricao']

    db.session.commit()

    return redirect(url_for("imoveis"))


@app.route("/imoveis/informacoes/<id>", methods=["GET", "POST"])
def continuar_cadastro(id):
    if not current_user.is_authenticated:
        return redirect(url_for("login"))
    
    # recupera os dados do imóvel
    imovel = Imovel.query.filter_by(id=id).first()

    if not imovel:
        return redirect(url_for("imoveis"))

    if request.method == "GET":
        return render_template("informacoes-imovel.html", imovel=imovel)

    # Recuperando arquivos
    # input_doc_imovel = request.files['doc_imovel']
    # input_doc_proprietario = request.files['doc_proprietario']
    input_capa = request.files['capa']

    # if input_doc_imovel.filename != '':
    #     filename = "doc_imovel-", str(imovel.id), ".pdf"
    #     path = os.path.join(app.config['UPLOAD_FOLDER'], "capas")
    #     # os.makedirs(path)
    #     input_capa.save(os.path.join(path, filename))
    #     imovel.doc_imovel = filename

    # if input_doc_proprietario.filename != '':
    #     filename = "doc_proprietario-", str(imovel.id), ".pdf"
    #     path = os.path.join(app.config['UPLOAD_FOLDER'], "capas")
    #     # os.makedirs(path)
    #     input_capa.save(os.path.join(path, filename))
    #     imovel.doc_proprietario = filename
    
    if input_capa.filename != '':
        filename = "capa-" + str(imovel.id) + ".jpg"
        path = os.path.join(app.config['UPLOAD_FOLDER'], "capas")
        # os.makedirs(path)
        input_capa.save(os.path.join(path, filename))
        imovel.capa = filename

    db.session.commit()

    return redirect(url_for("imoveis"))


@app.route("/imoveis/apagar/<id>", methods=["GET"])
def apagar_imovel(id):
    if not current_user.is_authenticated:
        return redirect(url_for("login"))
    
    # recupera os dados do imovel
    imovel = Imovel.query.filter_by(id=id).first()

    if not imovel:
        return redirect(url_for("imoveis"))

    # Apagando imovel
    db.session.delete(imovel)
    db.session.commit()

    return redirect(url_for("imoveis"))