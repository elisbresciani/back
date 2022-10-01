import jwt
from app import app
class Authenticate:
    @staticmethod
    def criar_token(idUsuario: int):
        payload = {'idUsuario': idUsuario, 'exp': 900000}
        token = jwt.encode(payload, app.config.get('SECRET_KEY'), app.config.get('ALGORITHM'))
        return token.decode('utf8')
    
    def autenticar_token(token: str):
        try:
            token_check = jwt.decode(token, app.config.get('SECRET_KEY'), app.config.get('ALGORITHM'))
            print(token_check)
            return {'idUsuario': token_check['idUsuario'] }, 200
        except jwt.exceptions.ExpiredSignatureError as e:
            return {'error': "O token expirou"}, 403
        except jwt.exceptions.InvalidTokenError as e:
            return {'error': "Token invalido"}, 403
        except Exception as e:
            return {'error': str(e)}, 403
    
    
