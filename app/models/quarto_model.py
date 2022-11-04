from app import db


class Quarto(db.Model):
    __tablename__ = "Quarto"
    id_quarto = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer)
    andar = db.Column(db.Integer)
    tipo = db.Column(db.String(150))
    preço = db.Column(db.Float)
    custo = db.Column(db.Float)
