from flask import Blueprint, json, Response, request

from app.models.quarto_model import Quarto

from app.serealizers.quarto_schema import QuartoSchema


class QuartoController(object):
    
    quarto_controller = Blueprint('quarto_controller', __name__)
    
    @quarto_controller.route('/quarto/consultar', methods=['GET'])
    def consultar_quarto():
        ...
        
    @quarto_controller.route('/quarto/consultar/<id_quarto>', methods=['GET'])
    def consultar_quarto_por_id(id_quarto):
        ...
        
        
    @quarto_controller.route('/quarto/cadatrar', methods=['POST'])
    def cadastrar_quarto():
        ...
        
    @quarto_controller.route('/quarto/alterar/<id_quarto>', methods=['PUT'])
    def alterar_quarto(id_quarto):
        ...
        
    @quarto_controller.route('/quarto/alterar/<id_quarto>', methods=['PATH'])
    def alterar_dados_quarto(id_quarto):
        ...
        
    @quarto_controller.route('/quarto/alterar/<id_quarto>', methods=['DELETE'])
    def deletar_quarto(id_quarto):
        ...
        
def custom_response(res, status_code):
    return Response(
        json.dumps(res),
        status=status_code, mimetype='application/json')