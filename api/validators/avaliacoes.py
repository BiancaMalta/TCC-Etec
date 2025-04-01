def validar_avaliacao(dados):
    nota = dados.get("nota")
    if nota is None or not (0 <= nota <= 5):
        return "A nota deve estar entre 0 e 5."
    return None
