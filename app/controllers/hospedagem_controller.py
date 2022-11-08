from flask import Blueprint, json, Response, request

from app.models.hospedagem_model import Hospedagem

from app.models.agenda_model import Agenda

from app.serealizers.hospedagem_schema import HospedagemSchema

from app.models.quarto_model import Quarto



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
        return custom_response({'mensagem': 'Deletado'}, 201)

    @hospedagem_controller.route('/hospedagem/cadastrar', methods=['POST'])
    def cadastra_hospedagem():  
        request_data = request.get_json()
        agenda = Agenda.query.filter_by(dia=request_data['check_in'])
        agenda.atualiazar_agenda(datetime=request_data['check_in'], quarto='quarto_1', id_quarto=request_data['id_quarto'])   
        
        data = hospedagem_schema.loads(request_data).data
        
        quarto_requisitado = data.get('quarto_id')
        if not Quarto.disponibilidade(quarto_requisitado):
            return custom_response({'mensagem': 'Erro ao cadastrar quarto não disponível'}, 401)
    
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
