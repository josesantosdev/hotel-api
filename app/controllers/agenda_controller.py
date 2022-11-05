from flask import Blueprint, json, Response, request
from app.models.agenda_model import Agenda
from app.serealizers.agenda_schema import AgendaSchema


class AgendaController(object):
    agenda_controller = Blueprint('agenda_controller', __name__)
    
    
    @agenda_controller.route('/disponiveis', methods=['GET'])
    def consultar_agenda():
        agenda = Agenda.quartos_disponiveis()
        serealized_agenda = agenda_schema.dump(agenda)
        return custom_response(serealized_agenda, 200)
    
    @agenda_controller.route('/atualizar/<date>', methods=['PATH'])
    def atualizar_agenda(date):
        request_data = request.get_json()
        agenda = Agenda.query.filter_by(dia=date).frist()
        agenda.atualizar(request_data)
        serealized_agenda = agenda_schema.dump(agenda)
        return custom_response(serealized_agenda, 200)
   
   
     
agenda_schema = AgendaSchema(many=True)


def custom_response(res, status_code):
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )