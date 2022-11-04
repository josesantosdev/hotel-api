from marshmallow import fields, Schema

from app.models.quarto_model import Quarto

class QuartoSchema(Schema):
    class Meta:
        
        model = Quarto
        load_instance = True
        
        id_quarto = fields.Int()
        numero = fields.Int()
        andar = fields.Int()
        tipo = fields.Str()
        preço = fields.Float()
        custo = fields.Float()
        disponibilidade = fields.Bool()