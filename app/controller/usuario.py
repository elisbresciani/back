from tkinter import E
from app.models.usuario import UsuarioModel
from app.repositorio.usuario import UsuarioRepositorio
from app.repositorio.endereco import EnderecoRepositorio
from app.models.endereco import EnderecoModel
import re
from flask import request

from app.Authenticate import Authenticate

class UsuarioController:
    def criar_usuario(args):
        try:
            usuario = UsuarioModel.from_dict(args)
            usuario.set_password(args.get("senha"))
            endereco = EnderecoModel.from_dict(args.get("endereco"))            
            retorno = EnderecoRepositorio.criar_endereco(endereco = endereco)
            if isinstance(retorno, Exception):
                return {'error': str(retorno)}, 500
            if retorno == True:  
                endereco_id = EnderecoRepositorio.last_inserted()
                if isinstance(endereco_id, dict):              
                    retorno_usuario = UsuarioRepositorio.criar_usuario(usuario = usuario, endereco_id = endereco_id.get("id"))
                    if isinstance(retorno_usuario, Exception):
                        return {'error': str(retorno_usuario)}, 500
                    if retorno_usuario == True:                  
                        usuario.set_idEndereco(endereco_id.get("id"))
                        endereco = EnderecoRepositorio.pega_endereco(usuario.idEndereco)
                        enderecoModel = EnderecoModel.from_dict(endereco)
                        usuario.setToken(None)
                        usuario_end = usuario.to_json(enderecoModel)
                        return usuario_end, 201
        except Exception as e:
            return {'error': str(e)}, 500
        
    
    def alterar_usuario(args):
        try:   
            usuario = UsuarioModel.from_dict(args)
            if args.get("senha"):
                usuario.set_password(args.get("senha"))
                no_pass = False
            elif not args.get("senha"):
                no_pass = True
            usuario.set_idUsuario(args.get("idUsuario"))
            UsuarioRepositorio.get_idEndereco(usuario= usuario)
            usuario.set_idEndereco(args.get("idEndereco"))
            endereco = EnderecoModel.from_dict(args.get("endereco"))
            endereco.set_idEndereco(usuario.idEndereco)
            retorno = EnderecoRepositorio.alterar_endereco(endereco)
            if isinstance(retorno, Exception):
                return {'error': str(retorno)}, 500
            if retorno == True: 
                retorno_usuario = UsuarioRepositorio.alterar_usuario(usuario = usuario, no_pass = no_pass)
                if isinstance(retorno_usuario, Exception):
                    return {'error': str(retorno_usuario)}, 500
                if retorno_usuario == True:
                    usuario_rep = UsuarioRepositorio.pega_usuario(usuario.idUsuario)
                    usuario.from_dict(usuario_rep)   
                    usuario.Senha = usuario_rep['Senha']               
                    token = Authenticate.criar_token(usuario.idUsuario)
                    usuario.setToken(token)
                    usuario_end = usuario.to_json(endereco)
                    return usuario_end, 201
        except Exception as e:
            return {'error': str(e)}, 500
            
    
    def pega_usuario(args):
        try:
            retorno_usuario = UsuarioRepositorio.pega_usuario(args.get('idUsuario'))
            if isinstance(retorno_usuario, Exception):
                return {'error': str(retorno_usuario)}, 500
            if retorno_usuario:
                usuario_model = UsuarioModel.from_dict(retorno_usuario)
                usuario_model.set_password(retorno_usuario['Senha'])
                usuario_model.set_idEndereco(retorno_usuario['idEndereco'])
                endereco = EnderecoRepositorio.pega_endereco(usuario_model.idEndereco)
                enderecoModel = EnderecoModel.from_dict(endereco)
                retorno = usuario_model.to_json(enderecoModel)
                return retorno, 200
        except Exception as e:
            return {'error': str(e)}, 500      
        
        
    def login(args):
        try:
            login = args.get('login')
            senha = args.get('senha')
            tipo = args.get('tipo')
            usuario = UsuarioModel
            retorno = {}
            retorno = UsuarioRepositorio.checa(login = login, tipo = tipo)
            if not isinstance(retorno, dict):
                return {'error': 'Login incorreto'}, 401
            if isinstance(retorno, Exception):
                return {'error': str(retorno)}, 500
            usuario = UsuarioModel.from_dict(retorno)
            usuario.Senha = retorno['Senha']
            usuario.set_idEndereco(retorno['idEndereco'])
            endereco = EnderecoRepositorio.pega_endereco(usuario.idEndereco)
            enderecoModel = EnderecoModel.from_dict(endereco)
            match = usuario.check_mach_passwords(senha)
            if match == True:
                token = Authenticate.criar_token(usuario.idUsuario)
                usuario.setToken(token)
                usuario_end = usuario.to_json(enderecoModel)
                return usuario_end, 200
            if match == False:
                return {'error': 'Senha incorreta'}, 401
        except Exception as e:
            return {'error': str(e)}, 500 
            
            
    def excluir(args):
        try:    
            retorno_usuario = UsuarioRepositorio.exclui(args.get("idUsuario"))
            if isinstance(retorno_usuario, Exception):
                return {'error': str(retorno_usuario)}, 500
            if retorno_usuario == True:
                return {'sucesso': "Usuario foi excluido"}, 200            
        except Exception as e:
            return {'error': str(e)}, 500
            