from flask import Blueprint
from app.controllers import patients_controller

bp_vaccination = Blueprint('bp_vaccination', __name__, url_prefix="/vaccinations")

bp_vaccination.post("")(patients_controller.create_patients)
bp_vaccination.get("")(patients_controller.retrieve_patients)