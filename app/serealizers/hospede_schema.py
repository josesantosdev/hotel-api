from marshmallow import fields, Schema

from app.models.hospede_model import Hospede


class HospedeSchema(Schema):
    class Meta:
        model = Hospede
        load_instance = True

        id_hospede = fields.Int()
        nome = fields.Str()
        cpf = fields.Str(required=True)
        endereco = fields.Str()
        email = fields.Email(required=True)
