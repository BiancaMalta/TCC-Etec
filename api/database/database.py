import sqlite3

DATABASE_PATH = "api/database/filmes.db"

def conectar():
    """Cria conexão com o banco de dados SQLite"""
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row  # Permite acessar colunas pelo nome
    return conn

def criar_tabelas():
    """Executa o script SQL para criar as tabelas"""
    conn = conectar()
    cursor = conn.cursor()
    with open("api/database/schema.sql", "r", encoding="utf-8") as f:
        cursor.executescript(f.read())
    conn.commit()
    conn.close()

def registrar_avaliacao(usuario_id, filme_id, nota, comentario=""):
    """Insere uma nova avaliação no banco"""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO avaliacoes (usuario_id, filme_id, nota, comentario) VALUES (?, ?, ?, ?)",
        (usuario_id, filme_id, nota, comentario),
    )
    conn.commit()
    conn.close()

def consultar_avaliacoes(filme_id):
    """Consulta todas as avaliações de um filme específico"""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT usuario_id, nota, comentario FROM avaliacoes WHERE filme_id = ?",
        (filme_id,),
    )
    avaliacoes = cursor.fetchall()
    conn.close()
    return [dict(avaliacao) for avaliacao in avaliacoes]  # Retorna como lista de dicionários

if __name__ == "__main__":
    criar_tabelas()
    print("Banco de dados e tabelas criados com sucesso!")
