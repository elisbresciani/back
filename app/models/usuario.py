from queue import Empty
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.endereco import EnderecoModel
import json

class UsuarioModel:
    idUsuario: int
    Nome: str
    Email: str
    CPF: str
    PIS: str
    Senha: str
    idEndereco: int
    Token: str
    
    @classmethod
    def from_dict(cls, dici): 
        cls.idUsuario = dici.get('idUsuario', None)
        cls.Nome = dici.get("nome") or dici['Nome']   
        cls.Email = dici.get("email") or dici['Email']
        cls.CPF = dici.get("cpf") or dici['CPF']
        cls.PIS = dici.get("pis") or dici['PIS']
        return cls()
    
    def set_idUsuario(self, idUsuario):
        self.idUsuario = idUsuario
    
    def set_password(self, password):  
        self.Senha = generate_password_hash(password)
        
    def set_password_return(password):  
       return generate_password_hash(password)
    
    def set_idEndereco(self, idEndereco):
        self.idEndereco = idEndereco
    
    def check_mach_passwords(self, password):
        return check_password_hash(self.Senha, password)
    
    def setToken(self, token):
        self.Token = token
    
    def to_json(self, endereco: EnderecoModel):
        return {
            "nome": self.Nome,
            "email": self.Email,
            "CPF": self.CPF,
            "PIS": self.PIS,
            "Senha": self.Senha,
            "idEndereco": self.idEndereco,
            "idUsuario": self.idUsuario,
            "endereco": endereco.to_json(),
            "token": self.Token
        }
        