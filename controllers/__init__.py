from flask import Blueprint
from flask_login import LoginManager
from ..models.user import User

from .auth import auth as auth_blueprint
from .welcome import welcome as welcome_blueprint
from .user import user as user_blueprint
from .overview import overview as overview_blueprint
from .contract import contract as contract_blueprint


login_manager = LoginManager()

login_manager.login_view = 'controllers.auth.login'


@login_manager.user_loader
def load_user(id):
    
    return User.query.get(int(id))


controllers = Blueprint('controllers', __name__)


def init_controllers():

    controllers.register_blueprint(auth_blueprint)
    
    controllers.register_blueprint(welcome_blueprint)
    
    controllers.register_blueprint(user_blueprint)
    
    controllers.register_blueprint(overview_blueprint)
    
    controllers.register_blueprint(contract_blueprint)
    
    
@controllers.after_request
def after_request_func(response):
    
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    
    response.headers['X-Content-Type-Options'] = 'nosniff'
    
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    
    return response