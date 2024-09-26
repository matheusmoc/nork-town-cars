from flask import Blueprint, Flask
from .car_routes import car
from .owner_routes import owner

api = Blueprint('api', __name__)
app = Flask(__name__)

api.register_blueprint(car, url_prefix='/cars/') 
api.register_blueprint(owner, url_prefix='/owners/') 

