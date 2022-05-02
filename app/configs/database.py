from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os

db = SQLAlchemy()

def init_app(app: Flask):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  

    db.init_app(app) 
    app.db = db

    from app.models.patient_model import Patient

    #db.create_all(app=app)



