from app import app
from app.resources.usuario import usuario_resources

class Routes: 
    @staticmethod
    def rotas():
        app.add_url_rule('/cadastro-usuario', 'cadastro-usuario', usuario_resources.criar_usuario, methods=['POST'])
        app.add_url_rule('/alterar', 'alterar', usuario_resources.alterar_usuario, methods=['POST'])
        app.add_url_rule('/usuario', 'usuario', usuario_resources.pega_usuario, methods=['GET'])
        app.add_url_rule('/login', 'login', usuario_resources.login, methods=['POST'])
        app.add_url_rule('/excluir', 'excluir', usuario_resources.excluir, methods=['POST'])
       
       
rotas = Routes()