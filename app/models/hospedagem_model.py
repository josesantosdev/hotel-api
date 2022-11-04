from app import db


class Hospedagem(db.Model):
    __tablename__ = 'Hospedagem'
    id_hospedagem = db.Column(db.Integer, primary_key=True)
