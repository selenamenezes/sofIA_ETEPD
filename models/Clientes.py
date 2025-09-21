import re
import hashlib

class Clientes:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = self.hash_senha(senha)
    
    @staticmethod
    def validar_senha(senha):
        if re.search(r"[^a-zA-Z0-9]", senha):
            return True
        return False
    
    @staticmethod
    def validar_email(email):
        if "@" in email and "." in email:
            return True
        return False
    
    @staticmethod
    def hash_senha(senha):
        senha_bytes = senha.encode('utf-8')
        hash_ = hashlib.sha256(senha_bytes)
        
        return hash_.hexdigest()
    