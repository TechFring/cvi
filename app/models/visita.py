from app import db


class Visita(db.Model):
    __tablename__ = "visita"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    id_imovel = db.Column(db.String(50), nullable=False, unique=True)
    id_corretor = db.Column(db.String(255), nullable=False)
    dia = db.Column(db.String(100), nullable=False, unique=True)
    nome_cliente = db.Column(db.String(100), nullable=False)
    telefone_cliente = db.Column(db.String(100), nullable=False)

    def __init__(self, id_imovel, id_corretor, dia, nome_cliente, telefone_cliente, capa, nome_corretor, dia_formatado):
        self.id_imovel = id_imovel
        self.id_corretor = id_corretor
        self.dia = dia
        self.nome_cliente = nome_cliente
        self.telefone_cliente = telefone_cliente
        self.capa = capa
        self.nome_corretor = nome_corretor
        self.dia_formatado = dia_formatado

    