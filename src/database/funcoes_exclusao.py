import sqlite3

# Conectar ao banco de dados
conexao = sqlite3.connect('gerenciador_de_leitura.db')
cursor = conexao.cursor()

# Função para deletar um livro pelo ID
def excluir_livro_por_id(id_livro):
    cursor.execute("DELETE FROM livros WHERE id_livro = ?", (id_livro,))
    conexao.commit()

    if cursor.rowcount > 0:
        print("Livro deletado com sucesso.")
    else:
        print("Livro com o ID informado não foi encontrado.")


#função para deletar um livro pelo titulo

def excluir_livro_por_titulo(titulo):
    cursor.execute('''
        DELETE FROM livros
        WHERE LOWER(titulo) = LOWER(?)
    ''', (titulo,))
    conexao.commit()

    if cursor.rowcount > 0:
        print(f"{cursor.rowcount} livro(s) com o título '{titulo}' foram excluídos com sucesso.")
    else:
        print(f"Nenhum livro com o título '{titulo}' foi encontrado.")

#função para deletar o livro pelo status

def excluir_livro_por_status(id_status):
    # Verifica se o status existe
    cursor.execute('SELECT * FROM status WHERE id_status = ?', (id_status,))
    if not cursor.fetchone():
        print(f"Status com ID {id_status} não existe.")
        return

    cursor.execute('''
        DELETE FROM livros
        WHERE id_status = ?
    ''', (id_status,))
    conexao.commit()

    if cursor.rowcount > 0:
        print(f"{cursor.rowcount} livro(s) com status ID {id_status} foram excluídos com sucesso.")
    else:
        print(f"Nenhum livro com status ID {id_status} foi encontrado.")

#função para deletar o livro pelo autor

def excluir_livros_por_autor(nome_autor):
    # Buscar o ID do autor
    cursor.execute('SELECT id_autor FROM autores WHERE LOWER(nome) = LOWER(?)', (nome_autor,))
    resultado = cursor.fetchone()

    if resultado:
        id_autor = resultado[0]

        # Excluir os livros associados a esse autor
        cursor.execute('DELETE FROM livros WHERE id_autor = ?', (id_autor,))
        conexao.commit()

        livros_excluidos = cursor.rowcount
        print(f"{livros_excluidos} livro(s) do autor '{nome_autor}' foram excluídos com sucesso.")
    else:
        print(f"Autor '{nome_autor}' não encontrado no banco de dados.")



#função para excluir todos os livros 

def excluir_todos_livros():
    # Deleta todos os registros da tabela livros
    cursor.execute('DELETE FROM livros')
    conexao.commit()
    print("Todos os livros foram deletados.")

    # Reseta o autoincremento da tabela livros
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='livros'")
    conexao.commit()
    print("Contador de ID da tabela 'livros' foi resetado.")