from app import db


class Reserva(db.Model):
    id_reserva = db.Column(db.Integer, primary_key=True)
