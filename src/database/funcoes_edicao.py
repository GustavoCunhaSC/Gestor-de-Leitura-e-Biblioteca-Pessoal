import sqlite3

# Conectar ao banco de dados
conexao = sqlite3.connect('gerenciador_de_leitura.db')
cursor = conexao.cursor()

# Função para editar o título de um livro (para editar você precisa primeiro digitar o
# id do livro do qual você quer editar o titulo, depois separe por virgula e escreva o novo nome do livro)
def editar_titulo_livro(id_livro, novo_titulo):
    cursor.execute('''
        UPDATE livros
        SET titulo = ?
        WHERE id_livro = ?
    ''', (novo_titulo, id_livro))
    conexao.commit()

    if cursor.rowcount > 0:
        print("Título do livro atualizado com sucesso.")
    else:
        print("Livro com o ID informado não foi encontrado.")


# Função para editar o nome do autor (para editar você precisa primeiro digitar o
# id do autor do qual você quer editar o nome, depois separe por virgula e escreva o novo nome do autor)

def editar_nome_autor(id_autor, novo_nome):
    cursor.execute('''
        UPDATE autores
        SET nome = ?
        WHERE id_autor = ?
    ''', (novo_nome, id_autor))
    conexao.commit()

    if cursor.rowcount > 0:
        print("Nome do autor atualizado com sucesso.")
    else:
        print("Autor com o ID informado não foi encontrado.")

# Função para editar o status do livro  (para editar você precisa primeiro digitar o
# id do do livro que você quer mudar o status, depois separe por virgula e digite numero o id do status que voce quer atualizar (lembrando que os id são 1 para lido, 2 para lendo, e 3 para quero ler))

def editar_status_livro(id_livro, novo_id_status):
    # Verifica se o status informado é válido
    cursor.execute('SELECT id_status FROM status WHERE id_status = ?', (novo_id_status,))
    status_existe = cursor.fetchone()

    if not status_existe:
        print(f"Status ID {novo_id_status} inválido. Use 1 (Lido), 2 (Lendo) ou 3 (Quero ler).")
        return

    # Atualiza o status do livro
    cursor.execute('''
        UPDATE livros
        SET id_status = ?
        WHERE id_livro = ?
    ''', (novo_id_status, id_livro))
    conexao.commit()

    if cursor.rowcount > 0:
        print("Status do livro atualizado com sucesso.")
    else:
        print("Livro com o ID informado não foi encontrado.")


























