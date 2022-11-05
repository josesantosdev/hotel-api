from app import db
from sqlalchemy.orm import relationship

class Hospedagem(db.Model):
    __tablename__ = 'Hospedagem'
    id_hospedagem = db.Column(db.Integer, primary_key=True)
    check_in = db.Column(db.DateTime)
    check_out = db.Column(db.DateTime)
    quarto_id = db.Column(db.Integer, db.ForeignKey('Quarto.id_quarto'))
    hospede_id = db.Column(db.Integer, db.ForeignKey('Hospede.id_hospede'))
    quarto = relationship('Quarto', backref='hospedagem')
    hospede = relationship('Hospede', backref='hospedagem')
    
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
        return Hospedagem.query.get(id_hospedagem)

    @staticmethod
    def todas_hospedagens():
        return Hospedagem.query.all()

    
