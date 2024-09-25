from flask import Flask
from .config import Config
from .models import db 
from .routes import api

def create_app(config_name=None):
    app = Flask(__name__)

    if config_name:
        app.config.from_object(config_name)
    else:
        app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(api)

    return app