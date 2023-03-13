import os
from flask import Flask, redirect, url_for, render_template, request
from flask_alembic import Alembic
from flask_login import LoginManager
from .models import db, contract, user, asso_user_contract


def create_app(test_config = None):
    
    app = Flask(__name__, instance_relative_config=True)

    login_manager = LoginManager()
    alembic = Alembic()

    DB_USERNAME = os.environ.get("DB_USERNAME")
    DB_PASSWORD = os.environ.get("DB_PASSWORD")
    DB_HOST = os.environ.get("DB_HOST")
    DB_PORT = os.environ.get("DB_PORT")
    DB_NAME = os.environ.get("DB_NAME")

    app.config['SECRET_KEY'] = 'dev'
    app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        
    db.init_app(app)
    alembic.init_app(app)
    login_manager.init_app(app)
       
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    with app.app_context():
        db.create_all()
        
    from .controllers.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    @app.route("/hello")
    def hello_world():
        return "<p>Hello, World!</p>"
    
    @app.route("/user-by-username/<username>", methods=['POST', 'GET'])
    def user_by_username(username):
        searched_user = db.session.execute(db.select(user.User).filter_by(user_name=username)).scalar_one()
        return render_template("show_user.html", user=searched_user)
    
    @login_manager.user_loader
    def load_user(user_id):
        return user.User.get(user_id)

    return app
