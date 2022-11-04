from app import db


class Hospede(db.Model):
    id_hospede = db.Column(db.Integer, primary_key=True)
