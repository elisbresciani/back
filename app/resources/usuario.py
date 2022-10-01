from app import app
from flask import request, jsonify
import json
from app.controller.usuario import UsuarioController

class UsuarioResources:
    def criar_usuario(self):              
        try:                  
            args = json.loads(request.data)
            retorno = UsuarioController.criar_usuario(args= args)
            return retorno
        except Exception as e:
            return jsonify({"error": str(e)}), 401
        
    def alterar_usuario(self):
        try:
            args = json.loads(request.data)
            retorno = UsuarioController.alterar_usuario(args= args)
            return retorno
        except Exception as e:
            return jsonify({"error": str(e)}), 401
        
    def pega_usuario(self):
        try:
            args = json.loads(request.data)
            retorno = UsuarioController.pega_usuario(args = args) 
            return retorno
        except Exception as e:
            return jsonify({"error": str(e)}), 401
        
        
    def login(self):
        try:            
            args = json.loads(request.data)
            retorno = UsuarioController.login(args = args) 
            return retorno
        except Exception as e:
            return jsonify({"error": str(e)}), 401
        
    def excluir(self):
        try:
            args = json.loads(request.data)
            retorno = UsuarioController.excluir(args = args) 
            return retorno
        except Exception as e:
            return jsonify({"error": str(e)}), 401
    
usuario_resources = UsuarioResources()