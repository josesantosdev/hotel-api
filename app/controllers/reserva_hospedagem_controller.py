from flask import Blueprint, json, Response, request

from app.models.reserva_hospedagem_model import ReservaHospedagem

from app.serealizers.reserva_hospedagem_schema import ReservaHospedagemSchema


class ReservaHospedagemController(object):

    reserva_hospedagem_controller = Blueprint('reserva_hospedagem_controller', __name__)

    @reserva_hospedagem_controller.route('/', methods=['GET'])
    def consultar_reserva_hospedagem():
        ...

    @reserva_hospedagem_controller.route('/', methods=['GET'])
    def consultar_reserva_hospedagem():
        ...
        
    @reserva_hospedagem_controller.route('/', methods=['POST'])
    def consultar_reserva_hospedagem():
        ...

    @reserva_hospedagem_controller.route('/', methods=['PUT'])
    def consultar_reserva_hospedagem():
        ...

    @reserva_hospedagem_controller.route('/', methods=['PATH'])
    def consultar_reserva_hospedagem():
        ...

    @reserva_hospedagem_controller.route('/', methods=['DELETE'])
    def consultar_reserva_hospedagem():
        ...

  

reserva_hospedagem_schema = ReservaHospedagemSchema()


def custom_response(res, status_code):
    return Response(
        json.dumps(res),
        status=status_code,
        mimetype='Application/json'
    )
