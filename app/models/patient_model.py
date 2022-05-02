from datetime import date
from app.configs.database import db
from sqlalchemy import String, DateTime, Column
from dataclasses import dataclass
from datetime import datetime,timedelta

@dataclass
class Patient(db.Model):

    cpf:str
    name: str
    first_shot_date: date
    second_shot_date: date
    vaccine_name: str
    health_unit_name: str

    
    __tablename__: "vaccine_cards"
    cpf = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    first_shot_date = Column(DateTime)
    second_shot_date = Column(DateTime)
    vaccine_name = Column(String, nullable=False)
    health_unit_name= Column(String)
