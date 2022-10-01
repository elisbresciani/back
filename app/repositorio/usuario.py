from sqlalchemy.sql import text
from app.models.usuario import UsuarioModel
from app import db, app
conn = db.create_engine(app.config.get('SQLALCHEMY_DATABASE_URI'), {})

class UsuarioRepositorio:
    def criar_usuario(usuario: UsuarioModel, endereco_id: int):
        try:
            
            query = text("""Insert into usuario(Nome, Email, CPF, PIS, Senha, idEndereco) values(:nome, :email, :cpf, :pis, :senha, :idendereco)""")
            retorno = conn.execute(query, 
                                        nome = usuario.Nome, 
                                        email = usuario.Email, 
                                        cpf = usuario.CPF, 
                                        pis = usuario.PIS, 
                                        senha = usuario.Senha, 
                                        idendereco = endereco_id,
                                    )
            return True
        except Exception as e:
            return e
    
    def alterar_usuario(usuario: UsuarioModel, no_pass: bool):
        try:
            if no_pass:
                query = text("""UPDATE usuario SET Nome = :nome, Email = :email, CPF = :cpf, PIS = :pis WHERE idUsuario = :idUsuario""")
                retorno = conn.execute(query, 
                                    nome = usuario.Nome, 
                                    email = usuario.Email, 
                                    cpf = usuario.CPF, 
                                    pis = usuario.PIS, 
                                    idUsuario = usuario.idUsuario
                                )
            elif not no_pass:
                query = text("""UPDATE usuario SET Nome = :nome, Email = :email, CPF = :cpf, PIS = :pis, Senha = :senha WHERE idUsuario = :idUsuario""")
                retorno = conn.execute(query, 
                                    nome = usuario.Nome, 
                                    email = usuario.Email, 
                                    cpf = usuario.CPF, 
                                    pis = usuario.PIS, 
                                    senha = usuario.Senha, 
                                    idUsuario = usuario.idUsuario
                                )
            return True
        except Exception as e:
            return e
        
    def get_idEndereco(usuario: UsuarioModel):
        try: 
            query = text("""Select idEndereco as id from usuario where idUsuario = :idUsuario""")
            retorno = conn.execute(query, idUsuario = usuario.idUsuario)
            rfo = retorno.fetchone()
            return dict(rfo)
        except Exception as e:
            return e
        
    def pega_usuario(idUsuario: int):
        try:
            query = text("""Select * from usuario where idUsuario = :idUsuario""")
            retorno = conn.execute(query, idUsuario = idUsuario)
            rfo = retorno.fetchone()
            return dict(rfo)
        except Exception as e:
            return e
        
    def checa(login: str, tipo: str):
        try:
            query = ""
            if tipo == 'Email':
                query = text("""Select * from usuario where Email = :login""")
            if tipo == 'CPF':
                query = text("""Select * from usuario where CPF = :login""")
            if tipo == 'PIS':
                query = text("""Select * from usuario where PIS = :login""")
            retorno = conn.execute(query, login = login)
            rfo = retorno.fetchone()
            return dict(rfo)
        except Exception as e:
            return e
        
    def exclui(idUsuario: int):
        try:
            query = text("""DELETE FROM usuario WHERE idUsuario = :idUsuario""")
            conn.execute(query, idUsuario = idUsuario)
            return True
        except Exception as e:
            return e
    
