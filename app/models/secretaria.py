from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def get_user(user_id):
    return Secretaria.query.filter_by(id=user_id).first()

class Secretaria(db.Model, UserMixin):
    __tablename__ = "secretaria"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    nome_usuario = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    senha = db.Column(db.String(100), nullable=False)

    def __init__(self, nome, nome_usuario, email, senha):
        self.nome = nome
        self.nome_usuario = nome_usuario
        self.email = email
        self.senha = generate_password_hash(senha)

    def verificar_senha(self, senha):
        return check_password_hash(self.senha, senha)
