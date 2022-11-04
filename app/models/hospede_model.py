from app import db


class Hospede(db.Model):
    __tablename__ = 'Hospede'
    id_hospede = db.Column(db.Integer, primary_key=True)
