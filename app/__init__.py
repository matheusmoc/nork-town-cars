from flask import Flask
from .models import db 
from .routes import api
from .auth import auth as auth_blueprint
from flask_login import LoginManager
from .models.user import User
import os
from flasgger import Swagger

def create_app(config_name=None):
    app = Flask(__name__)

    swagger = Swagger(app)

    env = os.getenv('FLASK_ENV', 'development')

    if env == 'production':
        app.config.from_object('app.config.ProductionConfig')
    elif env == 'testing':
        app.config.from_object('app.config.TestingConfig')
    else:
        app.config.from_object('app.config.DevelopmentConfig')

    db.init_app(app)

    app.register_blueprint(api)
    app.register_blueprint(auth_blueprint)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


    with app.app_context():
        db.create_all()

    return app