from tkinter import E
from flask import request, jsonify
from http import HTTPStatus
from app.models.patient_model import Patient
from app.configs.database import db
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import IntegrityError
from datetime import datetime,timedelta
def create_patients():

    class KeyError(Exception):
        pass

    class DataError(Exception):
        pass
    class StringError(Exception):
        pass
    try:   
        valid_keys = ['cpf', 'name', 'vaccine_name', 'health_unit_name', 'first_shot_date', 'second_shot_date']
               
        data = request.get_json()
        # def verify_keys(list_keys):
        #     key_list = []
        #     for item in list_keys.keys():                
        #         if item in valid_keys:
        #             key_list.append(item)
        #     return key_list

        # verifyed_keys = verify_keys(data)

        

        if data['cpf'].isnumeric == False or len(data['cpf']) != 11:
            raise DataError
  
        for item in data.values():
            print(data.values())
            if type(item) != str:
                raise StringError
        
        required_keys = ['cpf', 'name', 'vaccine_name', 'health_unit_name']
        get_data_keys = data.keys()
        for item in required_keys:
            if item not in get_data_keys:
                raise KeyError
       
        
        formated_data_patients = { 
            "cpf":data['cpf'].lower(),
            "name":data['name'].lower(),
            "first_shot_date":datetime.now().strftime("%d/%m/%Y %H:%M"),
            "second_shot_date": (datetime.now() + timedelta(days = 90)).strftime("%d/%m/%Y %H:%M"),
            "vaccine_name": data['vaccine_name'].lower(),
            "health_unit_name": data['health_unit_name'].lower()
        }

        print(formated_data_patients['first_shot_date'])
        print(formated_data_patients['second_shot_date']) 
        final_data = Patient(**formated_data_patients)       
                
        session: Session = db.session
        session.expire_on_commit = False
        session.add(final_data)
        session.add
        session.commit() 

        return jsonify(final_data), HTTPStatus.CREATED
    except DataError:
        return jsonify({"error": "Data error: CPF só contém números e precisa ter 11 digitos"}), HTTPStatus.BAD_REQUEST
    except StringError:
        return jsonify({"error": "Todos os campos precisam ser strings"}), HTTPStatus.BAD_REQUEST             
    except IntegrityError:
        return jsonify({"error": "CPF já existe"}), HTTPStatus.CONFLICT
    except KeyError:
        return jsonify({"error": "A requisição deverá ter os campos cpf, name, vaccine_name e health_unit_name"}), HTTPStatus.BAD_REQUEST


def retrieve_patients():
    database = (Patient.query.all())

    data_patients = [
        { 
            "cpf":patient.cpf,
            "name":patient.name,
            "first_shot_date":patient.first_shot_date,
            "second_shot_date":patient.second_shot_date,
            "vaccine_name": patient.vaccine_name,
            "health_unit_name":patient.health_unit_name
        } for patient in database
    ]


    return jsonify(data_patients), HTTPStatus.OK
    