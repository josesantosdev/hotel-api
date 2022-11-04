from app import db

class Quarto(db.Model):
    __tablename__ = "Quarto"
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer)