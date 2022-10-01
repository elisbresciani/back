from sqlalchemy.sql import text
from app.models.endereco import EnderecoModel
from app import db, app
conn = db.create_engine(app.config.get('SQLALCHEMY_DATABASE_URI'), {})

class EnderecoRepositorio:
    def criar_endereco(endereco: EnderecoModel):
        try:
            
            query = text("""Insert into endereco(Pais, Estado, Municipio, CEP, Rua, Numero, Complemento) values(:pais, :estado, :municipio, :cep, :rua, :numero, :complemento)""")
            retorno = conn.execute(query, 
                                        pais = endereco.Pais, 
                                        estado = endereco.Estado, 
                                        municipio = endereco.Municipio, 
                                        cep = endereco.CEP, 
                                        rua = endereco.Rua, 
                                        numero = endereco.Numero, 
                                        complemento = endereco.Complemento
                                    )  
            return True
        except Exception as e:
            return e
    
    def last_inserted():
        try: 
            query = text("""Select max(idEndereco) as id from endereco""")
            retorno = conn.execute(query)
            rfo = retorno.fetchone()
            return dict(rfo)
        except Exception as e:
            return e
        
        
    def alterar_endereco(endereco: EnderecoModel):
        try:
            query = text("""UPDATE endereco SET Pais = :pais, Estado = :estado, Municipio = :municipio, CEP = :cep, Rua = :rua, Numero = :numero, Complemento = :complemento WHERE idEndereco = :idEndereco""")
            retorno = conn.execute(query, 
                                    pais = endereco.Pais, 
                                    estado = endereco.Estado, 
                                    municipio = endereco.Municipio, 
                                    cep = endereco.CEP, 
                                    rua = endereco.Rua, 
                                    numero = endereco.Numero, 
                                    complemento = endereco.Complemento,
                                    idEndereco = endereco.idEndereco                                    
                                )
            return True
        except Exception as e:
            return e
        
        
    def pega_endereco(idEndereco: int):
        try:
            query = text("""Select * from endereco where idEndereco = :idEndereco""")
            retorno = conn.execute(query, idEndereco = idEndereco)
            rfo = retorno.fetchone()
            return dict(rfo)
        except Exception as e:
            return e