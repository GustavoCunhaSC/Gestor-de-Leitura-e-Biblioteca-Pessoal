# Este arquivo serve para inserir dados de exemplo no banco de dados biblioteca.db.
# Nele tem comandos pra adicionar autores, status de leitura e livros para testes e visualização.
# NÃO execute ele pra evitar criar dados duplicados no banco.

import sqlite3

# Conectar ao banco de dados
conexao = sqlite3.connect('gerenciador_de_leitura.db')
cursor = conexao.cursor()

# Inserir autores
autores = [
    ('Machado de Assis',),
    ('Clarice Lispector',),
    ('George Orwell',)
]
cursor.executemany('INSERT INTO autores (nome) VALUES (?)', autores)

# Inserir status
status_leitura = [
    ('Lido',),
    ('Lendo',),
    ('Quero ler',)
]
cursor.executemany('INSERT INTO status (descricao) VALUES (?)', status_leitura)

# Inserir livros
# Supondo que os autores e status inseridos têm IDs começando do 1
livros = [
    ('Dom Casmurro', 1, 1),  # Machado de Assis, Lido
    ('A Hora da Estrela', 2, 2),  # Clarice Lispector, Lendo
    ('1984', 3, 3)  # George Orwell, Quero ler
]
cursor.executemany('INSERT INTO livros (titulo, id_autor, id_status) VALUES (?, ?, ?)', livros)

# Salvar e fechar
conexao.commit()
conexao.close()

print("Dados de exemplo inseridos com sucesso!")
