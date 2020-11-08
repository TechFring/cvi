from app import app, db
from flask_login import current_user
from flask import render_template, request, redirect, url_for
import uuid
import os

# Models
from app.models.imovel import Imovel
from app.models.foto_interior import FotoInterior


# Rotas
@app.route("/imoveis", methods=["GET"])
def imoveis():
    if not current_user.is_authenticated:
        return redirect(url_for("login"))

    imoveis = Imovel.query.all()

    return render_template("imoveis.html", imoveis=imoveis)


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


@app.route("/imoveis/informacoes/<id>", methods=["GET"])
def informacoes_imovel(id):
    if not current_user.is_authenticated:
        return redirect(url_for("login"))

    # recupera os dados do imóvel
    imovel = Imovel.query.filter_by(id=id).first()

    if not imovel:
        return redirect(url_for("imoveis"))

    foto_interior = FotoInterior.query.filter_by(id_imovel=id).all()

    if request.method == "GET":
        return render_template("informacoes-imovel.html", imovel=imovel, foto_interior=foto_interior)


@app.route("/imoveis/informacoes/doc_imovel/<id>", methods=["POST"])
def imovel_doc_imovel(id):
    if not current_user.is_authenticated:
        return redirect(url_for("login"))

    # recupera os dados do imóvel
    imovel = Imovel.query.filter_by(id=id).first()

    if not imovel:
        return redirect(url_for("imoveis"))

    # Recuperando arquivos
    input_doc_imovel = request.files['doc_imovel']

    filename = "doc_imovel-" + str(imovel.id) + ".pdf"
    path = os.path.join(app.config['UPLOAD_FOLDER'], "docs")
    input_doc_imovel.save(os.path.join(path, filename))
    imovel.doc_imovel = filename

    db.session.commit()

    return redirect("/imoveis/informacoes/" + str(imovel.id))


@app.route("/imoveis/informacoes/doc_proprietario/<id>", methods=["POST"])
def imovel_doc_proprietario(id):
    if not current_user.is_authenticated:
        return redirect(url_for("login"))

    # recupera os dados do imóvel
    imovel = Imovel.query.filter_by(id=id).first()

    if not imovel:
        return redirect(url_for("imoveis"))

    # Recuperando arquivos
    input_doc_proprietario = request.files['doc_proprietario']

    filename = "doc_proprietario-" + str(imovel.id) + ".pdf"
    path = os.path.join(app.config['UPLOAD_FOLDER'], "docs")
    input_doc_proprietario.save(os.path.join(path, filename))
    imovel.doc_proprietario = filename

    db.session.commit()

    return redirect("/imoveis/informacoes/" + str(imovel.id))


@app.route("/imoveis/informacoes/capa/<id>", methods=["POST"])
def imovel_capa(id):
    if not current_user.is_authenticated:
        return redirect(url_for("login"))

    # recupera os dados do imóvel
    imovel = Imovel.query.filter_by(id=id).first()

    if not imovel:
        return redirect(url_for("imoveis"))

    # Recuperando arquivos
    input_capa = request.files['capa']

    filename = "capa-" + str(imovel.id) + ".jpg"
    path = os.path.join(app.config['UPLOAD_FOLDER'], "capas")
    input_capa.save(os.path.join(path, filename))
    imovel.capa = filename

    db.session.commit()

    return redirect("/imoveis/informacoes/" + str(imovel.id))


@app.route("/imoveis/informacoes/foto_interior/<id>", methods=["POST"])
def imovel_foto_interior(id):
    if not current_user.is_authenticated:
        return redirect(url_for("login"))

    # recupera os dados do imóvel
    imovel = Imovel.query.filter_by(id=id).first()

    if not imovel:
        return redirect(url_for("imoveis"))

    # Recuperando arquivos
    input_foto_interior = request.files['foto_interior']

    hash_foto = uuid.uuid4().hex

    filename = "foto_interior-" + str(imovel.id) + "-" + hash_foto + ".jpg"
    path = os.path.join(app.config['UPLOAD_FOLDER'], "fotos_interior")
    input_foto_interior.save(os.path.join(path, filename))

    foto_interior = FotoInterior(id, filename)

    db.session.add(foto_interior)
    db.session.commit()

    return redirect("/imoveis/informacoes/" + str(imovel.id))


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


@app.route("/imoveis/informacoes/<id_imovel>/foto_interior/apagar/<id>", methods=["GET"])
def apagar_foto_interior(id_imovel, id):
    if not current_user.is_authenticated:
        return redirect(url_for("login"))

    # recupera os dados do imóvel
    foto_interior = FotoInterior.query.filter_by(id=id).first()

    if not foto_interior:
        return redirect(url_for("imoveis"))

    db.session.delete(foto_interior)
    db.session.commit()

    return redirect("/imoveis/informacoes/" + str(id_imovel))