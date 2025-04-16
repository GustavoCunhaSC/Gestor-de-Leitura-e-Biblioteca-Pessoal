from database.banco import conectar

def cadastrar_usuario(nome, email, senha):
    conn = conectar()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)", (nome, email, senha))
        conn.commit()
        print("Usuário cadastrado com sucesso!")
        return True
    except Exception as e:
        print("Erro ao cadastrar usuário:", e)
        return False
    finally:
        conn.close()

def verificar_login(email, senha):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT id, nome FROM usuarios WHERE email = ? AND senha = ?", (email, senha))
    usuario = cursor.fetchone()

    conn.close()
    return usuario  # Retorna (id, nome) se encontrado, ou None