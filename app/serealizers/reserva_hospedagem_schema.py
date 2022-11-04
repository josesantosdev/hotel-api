from marshmallow import fields, Schema

from app.models.reserva_hospedagem_model import ReservaHospedagem


class ReservaHospedagemSchema(Schema):
    class Meta:
        
        model = ReservaHospedagem
        load_instance = True
        include_fk = True
        include_relationships = True
        
        id_reserva_hospedagem = fields.Int()
        check_in =  fields.DateTime()
        check_out = fields.DateTime()
        quarto_id = fields.Int(required=True)
        hospede_id = fields.Int(required=True)
        