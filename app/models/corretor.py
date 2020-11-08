from app import db


class Corretor(db.Model):
    __tablename__ = "corretor"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    creci = db.Column(db.String(50), nullable=False, unique=True)
    nome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    senha = db.Column(db.String(100), nullable=False)

    def __init__(self, creci, nome, email, senha):
        self.creci = creci
        self.nome = nome
        self.email = email
        self.senha = senha
