from app import db


class Quarto(db.Model):
    __tablename__ = "Quarto"
    id_quarto = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer)
    andar = db.Column(db.Integer)
    tipo = db.Column(db.String(150))
    preco = db.Column(db.Float)
    custo = db.Column(db.Float)
    disponibilidade = db.Column(db.Boolean)
    
    def __init__(self, data) -> None:
        self.numero = data.get('numero')
        self.andar = data.get('andar')
        self.tipo = data.get('tipo').lower
        self.preco = data.get('preco')
        self.custo = data.get('custo')
        self.disponibilidade = True
        
    
    
 
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
    def quarto_por_id(id_quarto):
        return Quarto.query.get(id_quarto)
    
    def quarto_disponível(self, quarto_id):
       quarto =  Quarto.query.filter(quarto_id=quarto_id)
       return quarto.disponibilidade

    @staticmethod
    def todos_quartos():
        return Quarto.query.all()

    def __repr__(self) -> str:
        return f'<id_quarto: {self.id_quarto}>'