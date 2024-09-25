from flask import Flask
from .config import Config
from .models import db 
from .routes import api
import os

def create_app(config_name=None):
    app = Flask(__name__)

    env = os.getenv('FLASK_ENV', 'development')

    if env == 'production':
        app.config.from_object('app.config.ProductionConfig')
    elif env == 'testing':
        app.config.from_object('app.config.TestingConfig')
    else:
        app.config.from_object('app.config.DevelopmentConfig')

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(api)

    return app