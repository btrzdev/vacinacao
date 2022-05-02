from flask import Blueprint, Flask
from app.routes.patient_route import bp_vaccination


def init_app(app: Flask):

    app.register_blueprint(bp_vaccination)