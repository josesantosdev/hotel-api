from flask import Blueprint, json, Response, request
from app.models.hospedagem_model import Hospedagem
from app.serealizers.hospedagem_schema import HospedagemSchema


class HospedagemController:

    hospedagem_controller = Blueprint('hospedagem_controller', __name__)

    @hospedagem_controller.route('/hospedagem', methods=['GET'])
    def consulta_hospedagem():
        hospedagem = Hospedagem.todas_hospedagens()
        serealized_hospedagem = hospedagem_schema.dump(hospedagem, many=True)
        return custom_response(serealized_hospedagem, 200)

    @hospedagem_controller.route('/hospedagem/atualizar/<id>', methods=['PUT'])
    def atualiza_hospedagem(id):
        request_data = request.get_json()
        hospedagem = Hospedagem.hospedagem_por_id(id)
        data = hospedagem_schema.load(request_data).data()
        hospedagem.atualizar(data)
        serealized_hospedagem = hospedagem_schema.dumps(hospedagem)
        return custom_response(serealized_hospedagem, 201)

    @hospedagem_controller.route('/hospedagem/deletar/<id>', methods=['DELETE'])
    def deleta_hospedagem():
        hospedagem = Hospedagem.hospedagem_por_id(id)
        hospedagem.deletar()
        serealized_hospedagem = hospedagem_schema.dumps(hospedagem)
        return custom_response({'mensagem': 'Deletado'}, 201)

    @hospedagem_controller.route('/hospedagem/cadastrar', methods=['POST'])
    def cadastra_hospedagem():
        request_data = request.get_json()
        data = hospedagem_schema.loads(request_data).data
        hospedagem = Hospedagem(data)
        hospedagem.salvar()
        serealized_hospedagem = hospedagem_schema.dump(hospedagem)
        return custom_response(serealized_hospedagem, 201)


hospedagem_schema = HospedagemSchema()


def custom_response(res, status_code):
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
