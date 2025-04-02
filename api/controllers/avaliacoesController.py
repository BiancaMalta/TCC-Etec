from flask import request, jsonify
from controllers.auth import verificar_autenticacao  # Middleware de autenticação
from database.database import registrar_avaliacao, consultar_avaliacoes
from validators.avaliacoes import validar_avaliacao

def post_avaliacao():
    dados = request.json
    usuario_id = request.user_id  # Assumindo que já foi autenticado pelo middleware
    filme_id = dados.get("filme_id")
    nota = dados.get("nota")
    comentario = dados.get("comentario", "")

    erro = validar_avaliacao(dados)
    if erro:
        return jsonify({"erro": erro}), 400

    avaliacao_id = registrar_avaliacao(usuario_id, filme_id, nota, comentario)
    return jsonify({"mensagem": "Avaliação registrada com sucesso!", "id": avaliacao_id}), 201

def get_avaliacoes(filme_id):
    avaliacoes = consultar_avaliacoes(filme_id)
    return jsonify({"filme_id": filme_id, "avaliacoes": avaliacoes})
