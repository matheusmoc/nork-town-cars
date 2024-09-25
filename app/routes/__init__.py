from flask import Blueprint
from .car_routes import car
from .owner_routes import owner

api = Blueprint('api', __name__)

api.register_blueprint(car, url_prefix='/cars/') 
api.register_blueprint(owner, url_prefix='/owners/') 

