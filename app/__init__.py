from json import load
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()

conn = os.getenv('STRING_CONNECTION')

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

