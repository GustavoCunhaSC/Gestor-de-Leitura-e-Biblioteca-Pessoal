import sqlite3

conexao = sqlite3.connect('gerenciador_de_leitura.db')
cursor = conexao.cursor()

# Tabela de usuários
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL
)
''')

# Tabela de autores
cursor.execute('''
CREATE TABLE IF NOT EXISTS autores (
    id_autor INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
)
''')

# Tabela de status
cursor.execute('''
CREATE TABLE IF NOT EXISTS status (
    id_status INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT NOT NULL
)
''')

# Tabela de livros (agora ligada a usuários)
cursor.execute('''
CREATE TABLE IF NOT EXISTS livros (
    id_livro INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    id_autor INTEGER,
    id_status INTEGER,
    id_usuario INTEGER,
    FOREIGN KEY (id_autor) REFERENCES autores(id_autor),
    FOREIGN KEY (id_status) REFERENCES status(id_status),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
)
''')

# Salva e fecha
conexao.commit()
conexao.close()

print("Banco de dados e tabelas criados com sucesso!")

