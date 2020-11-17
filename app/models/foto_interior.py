from app import db


class FotoInterior(db.Model):
    __tablename__ = "foto_interior"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    id_imovel = db.Column(db.Integer, db.ForeignKey("imovel.id", ondelete="CASCADE"), nullable=False)
    foto = db.Column(db.String(255), nullable=False)

    def __init__(self, id_imovel, foto):
        self.id_imovel = id_imovel
        self.foto = foto
