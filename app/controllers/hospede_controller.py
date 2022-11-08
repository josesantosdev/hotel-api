from flask import Blueprint, json, Response, request

from app.models.hospede_model import Hospede

from app.serealizers.hospede_schema import HospedeSchema

class HospedeController(object):
    
    hospede_controller = Blueprint('hospede_controller', __name__)
    
    @hospede_controller.route('/hospede/consultar', methods=['GET'])
    def consultar_hospede():
        hospede = Hospede.query.all()
        hospede_dumped = hospede_schema.dump(hospede)
        return custom_response(hospede_dumped, 200)
    
    @hospede_controller.route('/hospede/cadastrar', methods=['POST'])
    def cadastrar_hospede():
        request_data = request.get_json()
        data = hospede_schema.load(request_data)
        hospede = Hospede(data)
        hospede.salvar()
        serealized_hospede = hospede_schema.dump(hospede).data
        return custom_response(serealized_hospede, 201)
    
    
    @hospede_controller.route('/hospede/alterar/<hospede_id>', methods=['PUT'])
    def alterar_hospede(hospede_id):
        hospede = Hospede.query.filter_by(id=hospede_id).first_or_404()
        request_data = request.get_json()
        data = hospede_schema.load(request_data)
        hospede.atualizar(data)
        serealized_hospede = hospede_schema.dump(data).data
        return custom_response(serealized_hospede, 201)
    
    @hospede_controller.route('/hospede/alterar/<hospede_id>', methods=['PATH'])
    def alterar_dados_hospede(hospede_id):
        hospede = Hospede.query.filter_by(id=hospede_id).first_or_404()
        request_data = request.get_json()
        data = hospede_schema.load(request_data, partial=True)
        hospede.atualizar(data)
        serealized_hospede = hospede_schema.dump(data).data
        return custom_response(serealized_hospede, 201)
    
    @hospede_controller.route('/hospede/deletar/<hospede_id>', methods=['DELETE'])
    def deletar_hospede(hospede_id):
        hospede = Hospede.query.filter_by(hospede_id=hospede_id).first_or_404()
        hospede.deletar()
        return custom_response({'message': 'Deletado'}, 204)




hospede_schema = HospedeSchema()
hospedes_schema = HospedeSchema(many=True)

def custom_response(res, status_code):
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )
