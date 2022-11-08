from app import db

import datetime

from app.models.quarto_model import Quarto

class Agenda(db.Model):
    __tablename__ = 'Agenda'
    id_agenda = db.Column(db.Integer, primary_key=True)
    dia = db.Column(db.DateTime, nullable=False)
    quarto_1 = db.Column(db.Boolean)
    quarto_2 = db.Column(db.Boolean)
    quarto_3 = db.Column(db.Boolean)
    quarto_4 = db.Column(db.Boolean)
    quarto_5 = db.Column(db.Boolean)
    quarto_6 = db.Column(db.Boolean)
    quarto_7 = db.Column(db.Boolean)
    
    def atualizar(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        db.session.commit()
    
    @staticmethod
    def quartos_disponiveis(datetime):
        Agenda = Agenda.query.filter(datetime)
        return Agenda.all(True)
    
    def atualizar_agenda(self, datetime, quarto, id_quarto):
        agenda = Agenda.query.filter_by(dia=datetime).first()
        quarto = agenda.query.select(quarto)
        
        if quarto:
            pass
        else:
            quarto_indisponivel = Quarto.query.filter_by(id_quarto = id_quarto)
            quarto_indisponivel.atualizar({'disponibilidade': False})
        
    