from app import db, app
from 

conn = db.create_engine(app.config.get('SQLALCHEMY_DATABASE_URI'), {})
endereco = conn.execute('SELECT * FROM endereco')
result = endereco.fetchone()
print(result)