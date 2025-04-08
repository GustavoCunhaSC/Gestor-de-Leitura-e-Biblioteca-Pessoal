import sqlite3

# Conectar ao banco de dados
conexao = sqlite3.connect('biblioteca.db')
cursor = conexao.cursor()

# Função para consultar todos os livros junto com o nome do autor e status
def consultar_livros():
    cursor.execute('''
        SELECT 
            livros.id_livro,
            livros.titulo,
            autores.nome AS autor,
            status.descricao AS status
        FROM livros
        JOIN autores ON livros.id_autor = autores.id_autor
        JOIN status ON livros.id_status = status.id_status
    ''')
    resultados = cursor.fetchall()

    if resultados:
        for livro in resultados:
            print(f"ID: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}, Status: {livro[3]}")
    else:
        print("Nenhum livro encontrado.")

#função para consultar usando o titulo (Ela vai receber o título do livro
#e buscar no banco todos os livros com esse título, junto com o nome do autor e o status)

def consultar_por_titulo(titulo):
    cursor.execute('''
        SELECT 
            livros.id_livro,
            livros.titulo,
            autores.nome AS autor,
            status.descricao AS status
        FROM livros
        JOIN autores ON livros.id_autor = autores.id_autor
        JOIN status ON livros.id_status = status.id_status
        WHERE LOWER(livros.titulo) = LOWER(?)
    ''', (titulo,))
    resultados = cursor.fetchall()

    if resultados:
        for livro in resultados:
            print(f"ID: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}, Status: {livro[3]}")
    else:
        print("Nenhum livro encontrado com esse título.")


#função para consultar usando o autor (Ela vai receber o nome do autor
#e buscar no banco todos os livros escritos por esse autor o status)



def consultar_por_autor(nome_autor):
    cursor.execute('''
        SELECT 
            livros.id_livro,
            livros.titulo,
            autores.nome AS autor,
            status.descricao AS status
        FROM livros
        JOIN autores ON livros.id_autor = autores.id_autor
        JOIN status ON livros.id_status = status.id_status
        WHERE LOWER(autores.nome) = LOWER(?)
    ''', (nome_autor,))
    
    resultados = cursor.fetchall()

    if resultados:
        for livro in resultados:
            print(f"ID: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}, Status: {livro[3]}")
    else:
        print("Nenhum livro encontrado para este autor.")

#função para consultar usando o status (Ela vai receber o status
#e buscar no banco todos os livros com aquele status junto com o nome do autor)


def consultar_por_status(status):
    cursor.execute('''
        SELECT 
            livros.id_livro,
            livros.titulo,
            autores.nome AS autor,
            status.descricao AS status
        FROM livros
        JOIN autores ON livros.id_autor = autores.id_autor
        JOIN status ON livros.id_status = status.id_status
        WHERE LOWER(status.descricao) = LOWER(?)
    ''', (status,))
    resultados = cursor.fetchall()

    if resultados:
        for livro in resultados:
            print(f"ID: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}, Status: {livro[3]}")
    else:
        print(f"Nenhum livro com status '{status}' encontrado.")
