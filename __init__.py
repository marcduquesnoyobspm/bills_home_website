from flask import Flask
from flask_migrate import Migrate
from flask_moment import Moment
from flask_talisman import Talisman
from .controllers import login_manager, controllers, init_controllers
from .models import db, bcrypt
from .utils.config import Config


def create_app(config_class=Config):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(config_class)

    migrate = Migrate()
    moment = Moment()
    # talisman = Talisman()

    db.init_app(app)
    migrate.init_app(app, db)
    moment.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    # talisman.init_app(app, content_security_policy=None)

    init_controllers()

    app.register_blueprint(controllers)

    app.config.update(
        SESSION_COOKIE_SECURE=True,
        SESSION_COOKIE_HTTPONLY=True,
        SESSION_COOKIE_SAMESITE="Lax",
    )

    return app
