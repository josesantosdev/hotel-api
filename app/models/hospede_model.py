from app import db


class Hospede(db.Model):
    # atributos
    __tablename__ = 'Hospede'
    id_hospede = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    cpf = db.Column(db.Integer, nullable=False, unique=True)
    endereco = db.Column(db.String(255))
    email = db.Column(db.String(255), nullable=False, unique=True)
    
    def __init__(self, data):
        self.nome = data.get('nome')
        self.cpf = data.get('cpf')
        self.endereco = data.get('endereco')
        self.email = data.get('email')

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
    def hospede_por_id(id_hospede):
        return Hospede.query.get(id_hospede)

    @staticmethod
    def todos_hospedes():
        return Hospede.query.all()

    def __repr__(self) -> str:
        return f'<id_hospede: {self.id_hospede}>'
