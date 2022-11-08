from flask import Blueprint, json, Response, request

from app.models.quarto_model import Quarto

from app.serealizers.quarto_schema import QuartoSchema


class QuartoController(object):
    
    quarto_controller = Blueprint('quarto_controller', __name__)
    
    @quarto_controller.route('/quarto/consultar', methods=['GET'])
    def consultar_quarto():
        quarto = Quarto.query.all()
        serealized_quarto = quarto_schema.dump(quarto, many=True)
        return custom_response(serealized_quarto, 200)
        
    @quarto_controller.route('/quarto/consultar/<id_quarto>', methods=['GET'])
    def consultar_quarto_por_id(id_quarto):
        quarto = Quarto.query.filter_by(id_quarto=id_quarto).first_or_404()
        serealized_quarto = quarto_schema.dump(quarto)
        return custom_response(serealized_quarto, 200)
        
        
    @quarto_controller.route('/quarto/cadatrar', methods=['POST'])
    def cadastrar_quarto():
        request_data = request.get_json()
        data = quarto_schema.load(request_data)
        quarto = Quarto(data)
        quarto.salvar()
        serealized_quarto = quarto_schema.dump(quarto)
        return custom_response(serealized_quarto, 201)
        
    @quarto_controller.route('/quarto/alterar/<id_quarto>', methods=['PUT'])
    def alterar_quarto(id_quarto):
        dados_requisicao = request.get_json()
        quarto = Quarto.query.filter_by(id_quarto=id_quarto).first()
        dados = quarto_schema.load(dados_requisicao)
        quarto.alterar(dados)
        serealized_quarto = quarto_schema.dump(quarto)
        return custom_response(serealized_quarto, 201)        
        
        
        
    @quarto_controller.route('/quarto/alterar/<id_quarto>', methods=['PATH'])
    def alterar_dados_quarto(id_quarto):
        dados_requisicao = request.get_json()
        quarto = Quarto.query.filter_by(id_quarto=id_quarto).first()
        dados = quarto_schema.load(dados_requisicao, partial=True)
        quarto.alterar(dados)
        serealized_quarto = quarto_schema.dump(quarto, partial=True)
        return custom_response(serealized_quarto, 201)     
        
    @quarto_controller.route('/quarto/alterar/<id_quarto>', methods=['DELETE'])
    def deletar_quarto(id_quarto):
        quarto = Quarto.query.filter_by(id_quarto=id_quarto).frist_or_404()
        quarto.deletar()
        return custom_response({'mensagem': 'Deletado'}, 201)

quarto_schema = QuartoSchema()


def custom_response(res, status_code):
    return Response(
        json.dumps(res),
        status=status_code, mimetype='application/json')