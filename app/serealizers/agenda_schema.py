from marshmallow import fields, Schema

from app.models.agenda_model import Agenda

class AgendaSchema(Schema):
    class Meta:
        model = Agenda
        load_instance = True
        
        
        dia = fields.DateTime()
        quarto_1 = fields.Bool()
        quarto_2 = fields.Bool()
        quarto_3 = fields.Bool()
        quarto_4 = fields.Bool()
        quarto_5 = fields.Bool()
        quarto_6 = fields.Bool()
        quarto_7 = fields.Bool()