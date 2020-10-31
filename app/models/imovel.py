from app import db


class Imovel(db.Model):
    __tablename__ = "imovel"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    endereco = db.Column(db.String(255), nullable=False)
    latitude = db.Column(db.String(100))
    longitude = db.Column(db.String(100))
    tamanho = db.Column(db.Integer, nullable=False)
    quartos = db.Column(db.Integer, nullable=False)
    banheiros = db.Column(db.Integer, nullable=False)
    garagem = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.String(255), nullable=False)
    doc_imovel = db.Column(db.String(255))
    doc_proprietario = db.Column(db.String(255))
    capa = db.Column(db.String(255))

    def __init__(self, endereco, latitude, longitude, tamanho, quartos, banheiros, garagem, descricao, doc_imovel, doc_proprietario, capa):
        self.endereco = endereco
        self.latitude = latitude
        self.longitude = longitude
        self.tamanho = tamanho
        self.quartos = quartos
        self.banheiros = banheiros
        self.garagem = garagem
        self.descricao = descricao
        self.doc_imovel = doc_imovel
        self.doc_proprietario = doc_proprietario
        self.capa = capa
