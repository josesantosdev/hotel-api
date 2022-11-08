from flask import Blueprint, json, Response, request

from app.models.reserva_hospedagem_model import ReservaHospedagem

from app.serealizers.reserva_hospedagem_schema import ReservaHospedagemSchema


class ReservaHospedagemController(object):

    reserva_hospedagem_controller = Blueprint('reserva_hospedagem_controller', __name__)

    @reserva_hospedagem_controller.route('/reserva/consultar', methods=['GET'])
    def consultar_reserva_hospedagem():
        reserva_hospedagem = ReservaHospedagem.query.all()
        serealized_reserva_hospedagem = reserva_hospedagem_schema.dump(reserva_hospedagem, many=True)
        return custom_response(serealized_reserva_hospedagem, 200)
    

    @reserva_hospedagem_controller.route('/reserva/consultar/<id_reserva>', methods=['GET'])
    def consultar_reserva_hospedagem_por_id(id_reserva):
        reserva_hospedagem = ReservaHospedagem.query.filter_by(id_reserva=id_reserva).first_or_404()
        serealized_reserva_hospedagem = reserva_hospedagem_schema.dump(reserva_hospedagem)
        return custom_response(serealized_reserva_hospedagem, 200)
    
        
    @reserva_hospedagem_controller.route('/reserva/cadastrar', methods=['POST'])
    def cadastrar_reserva_hospedagem():
        request_data =  request.get_json()
        data = reserva_hospedagem_schema.load(request_data).data
        reserva_hospedagem = ReservaHospedagem(data)
        reserva_hospedagem.salvar()
        serealized_reserva_hospedagem = reserva_hospedagem_schema.dump(reserva_hospedagem)
        return custom_response(serealized_reserva_hospedagem, 201)
        

    @reserva_hospedagem_controller.route('/reserva/atualizar/<id_reserva>', methods=['PUT'])
    def alterar_reserva_hospedagem(id_reserva):
        request_data =  request.get_json()
        data = reserva_hospedagem_schema.load(request_data)
        reserva_hospedagem = ReservaHospedagem.query.filter_by(id_reserva=id_reserva).first_or_404()
        reserva_hospedagem.atualizar(data)
        serealized_reserva_hospedagem = reserva_hospedagem_schema.dump(reserva_hospedagem).data
        return custom_response(serealized_reserva_hospedagem, 201)
        

    @reserva_hospedagem_controller.route('/reserva/atualizar/<id_reserva>', methods=['PATH'])
    def alterar_dados_reserva_hospedagem(id_reserva):
        request_data =  request.get_json()
        data = reserva_hospedagem_schema.load(request_data, partial=True)
        reserva_hospedagem = ReservaHospedagem.query.filter_by(id_reserva=id_reserva).first_or_404()
        reserva_hospedagem.atualizar(data)
        serealized_reserva_hospedagem = reserva_hospedagem_schema.dump(reserva_hospedagem, partial=True).data
        return custom_response(serealized_reserva_hospedagem, 201)
    

    @reserva_hospedagem_controller.route('/reserva/deletar/<id_reserva>', methods=['DELETE'])
    def deletar_reserva_hospedagem(id_reserva):
        reserva_hospedagem = ReservaHospedagem.query.filter_by(id_reserva=id_reserva).first_or_404()
        reserva_hospedagem.deletar()
        return custom_response({'Mensagem': 'deletado'}, 201)
        

  

reserva_hospedagem_schema = ReservaHospedagemSchema()


def custom_response(res, status_code):
    return Response(
        json.dumps(res),
        status=status_code,
        mimetype='Application/json'
    )
