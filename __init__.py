import os
from flask import Flask, redirect, url_for, render_template, request
from flask_migrate import Migrate
from .controllers import login_manager
from .models import db, contract, user, asso_user_contract, bcrypt
from .utils.config import Config


def create_app(config_class=Config):
    
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(config_class)
    
    migrate = Migrate()
        
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    bcrypt.init_app(app)
        
    from .controllers.auth import auth as auth_blueprint
    from .controllers.index import index as index_blueprint
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(index_blueprint)
    
    @login_manager.user_loader
    def load_user(id):
        return user.User.query.get(int(id))

    return app
