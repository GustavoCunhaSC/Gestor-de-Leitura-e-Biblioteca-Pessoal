import sqlite3

conexao = sqlite3.connect('biblioteca.db')
cursor = conexao.cursor()

#função para inserir livro com validação
def inserir_livro(titulo, id_autor, id_status):
    if not titulo.strip():
        print("Erro: O título do livro não pode estar vazio.")
        return
    
    if not id_autor:
        print("Erro: O ID do autor é obrigatório.")
        return

    if not id_status:
        print("Erro: O ID do status é obrigatório.")
        return

    cursor.execute('''
        INSERT INTO livros (titulo, id_autor, id_status)
        VALUES (?, ?, ?)
    ''', (titulo, id_autor, id_status))
    conexao.commit()
    print("Livro inserido com sucesso!")

#função inserir autor com validação
def inserir_autor(nome,):
    if not nome.strip():
        print("Erro: O nome do autor não pode estar vazio.")
        return
    
    cursor.execute('''
        INSERT INTO autores (nome)
        VALUES (?)
    ''', (nome,) )
    conexao.commit()
    print("Autor inserido com sucesso!")

#função inserir status com validação
def inserir_status(descricao):
    if not descricao.strip():
        print("Erro: A descrição do status não pode estar vazia.")
        return
    
    cursor.execute('''
        INSERT INTO status (descricao)
        VALUES (?)
    ''', (descricao,))
    conexao.commit()
    print("Status inserido com sucesso!")



