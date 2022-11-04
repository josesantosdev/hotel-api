from app import db
from sqlalchemy.orm import relationship


class ReservaHospedagem(db.Model):
    __tablename__ = 'ReservaHospedagem'
    id_reserva_hospedagem = db.Column(db.Integer, primary_key=True)
    check_in = db.Column(db.DateTime)
    check_out = db.Column(db.DateTime)
    quarto_id = db.Column(db.Integer, db.ForeignKey('Quarto.id_quarto'))
    hospede_id = db.Column(db.Integer, db.ForeignKey('Hospede.id_hospede'))
    quarto = relationship('Quarto', backref='ReservaHospedagem')
    hospede = relationship('Hospede', backref='ReservaHospedagem')
    
  # metodos banco de dados
    def salvar(self):
        db.session.add(self)
        db.session.commit()

    def atualizar(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        db.session.commit()

    def deletar(self):
        db.session.delete(self)
        db.session.commit()
        
    # metodos de no querys banco
    @staticmethod
    def hospedagem_por_id(id_hospedagem):
        return ReservaHospedagem.query.get(id_hospedagem)

    @staticmethod
    def todos_hospedagens():
        return ReservaHospedagem.query.all()
