import sqlite3

conexao = sqlite3.connect('gerenciador_de_leitura.db')
cursor = conexao.cursor()


#função para inserir livro com validação
#essa função serve para: 
# Verificar se o autor já existe na tabela autores.
# Se não existir, vai inseri-lo automaticamente.
# Verificar se o id_status informado é válido (1, 2 ou 3).
# Inserir o livro com o id_autor e id_status.

def inserir_livro(titulo, nome_autor, id_status):

    # Verifica se o status informado é válido
    cursor.execute("SELECT id_status FROM status WHERE id_status = ?", (id_status,))
    status_valido = cursor.fetchone()
    if not status_valido:
        print(f"Status ID {id_status} inválido. Use 1 (Lido), 2 (Lendo) ou 3 (Quero ler).")
        conexao.close()
        return

    # Verifica se o autor já existe
    cursor.execute("SELECT id_autor FROM autores WHERE LOWER(nome) = LOWER(?)", (nome_autor,))
    resultado = cursor.fetchone()

    if resultado:
        id_autor = resultado[0]
    else:
        # Insere o autor e obtém o novo id_autor
        cursor.execute("INSERT INTO autores (nome) VALUES (?)", (nome_autor,))
        id_autor = cursor.lastrowid

    # Insere o livro com id_autor e id_status
    cursor.execute("INSERT INTO livros (titulo, id_autor, id_status) VALUES (?, ?, ?)", (titulo, id_autor, id_status))
    conexao.commit()
    conexao.close()
    print(f"Livro '{titulo}' inserido com sucesso!")