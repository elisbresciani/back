import json
class EnderecoModel:
    idEndereco: int
    Pais: str
    Estado: str
    Municipio: str
    CEP: str
    Rua: str
    Numero: str
    Complemento: str
    
    
    @classmethod
    def from_dict(cls, dict): 
        cls.Pais = dict.get("pais") or dict['Pais']
        cls.Estado = dict.get("estado") or dict['Estado']
        cls.Municipio = dict.get("municipio") or dict['Municipio']
        cls.CEP = dict.get("cep") or dict['CEP']
        cls.Rua = dict.get("rua") or dict['Rua']
        cls.Numero = dict.get("numero") or dict['Numero']
        cls.Complemento = dict.get("complemento") or dict['Complemento']
        return cls()
    
    def set_idEndereco(self, idEndereco: int):
        self.idEndereco = idEndereco
        
    def to_json(self):
        return {
            "Pais": self.Pais,
            "Estado": self.Estado,
            "Municipio": self.Municipio,
            "CEP": self.CEP,
            "Rua": self.Rua,
            "Numero": self.Numero,
            "Complemento": self.Complemento
        }