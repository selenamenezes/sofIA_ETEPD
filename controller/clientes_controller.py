from database.db import conexao
from models.Clientes import Clientes

def cadastro_cliente(nome, email, senha, confirm_senha):
    if not Clientes.validar_email(email):
        return False, "Formato inválido de E-mail."
    
    if not Clientes.validar_senha(senha):
        return False, "Senha inválida. Insira pelo menos um caractere especial."
    
    if senha != confirm_senha:
        return False, "As senhas não coincidem."

    cliente = Clientes(nome.title(), email, senha)
    try:
        conn = conexao()
        cursor = conn.cursor()
        
        cursor.execute("insert into clientes (nome, email, senha) values (?, ?, ?)", (cliente.nome, cliente.email, cliente.senha))
        conn.commit()
    except Exception as e:
        return False, f"Erro ao cadastrar usuário: {e}"
    finally:
        conn.close()
    
    return True, "Cadastro concluído!"

def login_cliente(email, senha):
    try:
        conn = conexao()
        cursor = conn.cursor()

        if not Clientes.validar_email(email):
            return False, "Formato inválido de E-mail."

        cursor.execute("select senha from clientes where email = ?", (email, ))
        registro = cursor.fetchone()

        if registro:
            hash_ = Clientes.hash_senha(senha)
            if hash_ == registro[0]:
                return True, "Bem vindo(a)!"
            else:
                return False, "Senha incorreta!"
        else:
            return False, "E-mail não encontrado."
        
    except Exception as e:
        return False, f"Erro ao tentar logar: {e}"
    finally:
        conn.close()