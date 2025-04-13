from .banco import conectar
from database.sessao_usuario import get_usuario_logado

def inserir_ou_obter_autor(nome, nacionalidade=None):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM autores WHERE LOWER(nome) = LOWER(?)", (nome,))
    resultado = cursor.fetchone()

    if resultado:
        autor_id = resultado[0]
    else:
        cursor.execute("INSERT INTO autores (nome, nacionalidade) VALUES (?, ?)", (nome, nacionalidade))
        autor_id = cursor.lastrowid

    conn.commit()
    conn.close()
    return autor_id


def inserir_livro(titulo, autor_id, status, data_inicio=None, data_fim=None):
    from database.sessao_usuario import get_usuario_logado
    usuario = get_usuario_logado()
    if usuario is None:
        print("Nenhum usuário logado.")
        return
    usuario_id = usuario[0]

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO livros (titulo, autor_id, status, data_inicio, data_fim, usuario_id)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (titulo, autor_id, status, data_inicio, data_fim, usuario_id))

    conn.commit()
    conn.close()




def listar_autores():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT id, nome, nacionalidade FROM autores")
    autores = cursor.fetchall()

    conn.close()
    return autores


def listar_livros(status=None):
    from database.sessao_usuario import get_usuario_logado

    usuario = get_usuario_logado()
    usuario_id = usuario[0]  # pega só o ID

    if usuario_id is None:
        print("Nenhum usuário logado.")
        return []

    conn = conectar()
    cursor = conn.cursor()

    if status:
        cursor.execute('''
            SELECT livros.id, livros.titulo, autores.nome, livros.status, livros.data_inicio, livros.data_fim
            FROM livros
            JOIN autores ON livros.autor_id = autores.id
            WHERE livros.status = ? AND livros.usuario_id = ?
        ''', (status, usuario_id))
    else:
        cursor.execute('''
            SELECT livros.id, livros.titulo, autores.nome, livros.status, livros.data_inicio, livros.data_fim
            FROM livros
            JOIN autores ON livros.autor_id = autores.id
            WHERE livros.usuario_id = ?
        ''', (usuario_id,))

    resultados = cursor.fetchall()
    conn.close()
    return resultados



def atualizar_livro(id_livro, novo_titulo, novo_status, nova_data_inicio, nova_data_fim):
    from database.sessao_usuario import get_usuario_logado
    usuario_id = get_usuario_logado()[0]
    if usuario_id is None:
        print("Nenhum usuário logado.")
        return

    conn = conectar()
    cursor = conn.cursor()

    # Verifica se o livro pertence ao usuário
    cursor.execute("SELECT id FROM livros WHERE id = ? AND usuario_id = ?", (id_livro, usuario_id))
    if cursor.fetchone() is None:
        print("Você não tem permissão para editar este livro.")
        conn.close()
        return

    cursor.execute('''
        UPDATE livros
        SET titulo = ?, status = ?, data_inicio = ?, data_fim = ?
        WHERE id = ? AND usuario_id = ?
    ''', (novo_titulo, novo_status, nova_data_inicio, nova_data_fim, id_livro, usuario_id))
    
    conn.commit()
    conn.close()



def excluir_livro(id_livro):
    from database.sessao_usuario import get_usuario_logado
    usuario_id = get_usuario_logado()[0]

    if usuario_id is None:
        print("Nenhum usuário logado.")
        return

    conn = conectar()
    cursor = conn.cursor()

    # Verifica se o livro pertence ao usuário
    cursor.execute("SELECT id FROM livros WHERE id = ? AND usuario_id = ?", (id_livro, usuario_id))
    if cursor.fetchone() is None:
        print("Você não tem permissão para excluir este livro.")
        conn.close()
        return

    cursor.execute('DELETE FROM livros WHERE id = ? AND usuario_id = ?', (id_livro, usuario_id))
    conn.commit()
    conn.close()

