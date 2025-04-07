import sqlite3

conexao = sqlite3.connect('biblioteca.db')
cursor = conexao.cursor()

#tabela de autores 
cursor.execute('''
CREATE TABLE autores (
    id_autor INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
)
''')

#tabela de status
cursor.execute('''
CREATE TABLE status (
    id_status INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT NOT NULL
)
''')

#tabela de livros
cursor.execute('''
CREATE TABLE IF NOT EXISTS livros (
    id_livro INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    id_autor INTEGER,
    id_status INTEGER,
    FOREIGN KEY (id_autor) REFERENCES autores(id_autor),
    FOREIGN KEY (id_status) REFERENCES status(id_status)
)
''')

# Salva as alterações e fecha a conexão
conexao.commit()
conexao.close()

print("Banco de dados e tabelas criados com sucesso!")