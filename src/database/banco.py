import sqlite3
import os

def conectar():
    caminho_db = os.path.join(os.path.dirname(os.path.dirname(__file__)), "biblioteca.db")
    return sqlite3.connect(caminho_db)

def criar_tabelas():
    conn = conectar()
    cursor = conn.cursor()

    # Criar tabela usuarios
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL
        );
    ''')

    # Criar tabela autores
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS autores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            nacionalidade TEXT
        );
    ''')

    # Criar tabela livros
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL,
        status TEXT NOT NULL,
        data_inicio TEXT,
        data_fim TEXT,
        caminho_pdf TEXT,
        usuario_id INTEGER NOT NULL,
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
    );
""")


    conn.commit()
    conn.close()

# Executar ao rodar o script
criar_tabelas()
