from flask import Blueprint
from controllers.avaliacoes import post_avaliacao, get_avaliacoes

avaliacoes_bp = Blueprint("avaliacoes", __name__)

avaliacoes_bp.route("/api/avaliacoes", methods=["POST"])(post_avaliacao)
avaliacoes_bp.route("/api/avaliacoes/<int:filme_id>", methods=["GET"])(get_avaliacoes)
