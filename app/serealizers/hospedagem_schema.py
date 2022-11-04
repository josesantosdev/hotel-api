from marshmallow import fields, Schema

from app.models.hospedagem_model import Hospedagem


class HospedagemSchema(Schema):
    class Meta:
        model = Hospedagem
        load_instance = True
        include_fk = True
        include_relationships = True
        
        id_hospedagem = fields.Str(dump_only=True)
        check_in = fields.DateTime()
        check_out = fields.DateTime()
        quarto_id = fields.Int(required=True)
        hospede_id = fields.Int(required=True)
        