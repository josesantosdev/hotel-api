from app import db


class ReservaHospedagem(db.Model):
    __tablename__ = 'ReservaHospedagem'
    id_reserva = db.Column(db.Integer, primary_key=True)
