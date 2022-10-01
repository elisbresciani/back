from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

conn = "mysql://root:123456@localhost:3306/mydb"

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = conn
app.config['SECRET_KEY'] = '123456'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['ALGORITHM'] = "HS256"

CORS(app)
cors = CORS(app, resources={
    r"/":{
        "origins": ""
    }
})
db = SQLAlchemy(app)

