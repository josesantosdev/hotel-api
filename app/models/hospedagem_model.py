from app import db


class Hospedagem(db.Model):
    id_hospedagem = db.Column(db.Integer, primary_key=True)
