from flask import Flask, redirect, url_for, render_template, request
from flask_migrate import Migrate
from flask_moment import Moment
from .controllers import login_manager
from .models import db, bcrypt
from .utils.config import Config


def create_app(config_class=Config):

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(config_class)

    migrate = Migrate()
    moment = Moment()

    db.init_app(app)
    migrate.init_app(app, db)
    moment.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    from .controllers.auth import auth as auth_blueprint
    from .controllers.welcome import welcome as welcome_blueprint
    from .controllers.profile import profile as profile_blueprint
    from .controllers.overview import overview as overview_blueprint
    from .controllers.contract import contract as contract_blueprint
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(welcome_blueprint)
    app.register_blueprint(profile_blueprint)
    app.register_blueprint(overview_blueprint)
    app.register_blueprint(contract_blueprint)

    return app
