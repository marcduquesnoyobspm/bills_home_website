from flask import Flask, redirect, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_alembic import Alembic
from flaskr.database import db

import os
from models import contract, user, asso_user_contract


def create_app(test_config = None):
    
    app = Flask(__name__, instance_relative_config=True)
    
    alembic = Alembic()

    DB_USERNAME = os.environ['DB_USERNAME']
    DB_PASSWORD = os.environ["DB_PASSWORD"]
    DB_HOST = os.environ["DB_HOST"]
    DB_PORT = os.environ["DB_PORT"]
    DB_NAME = os.environ["DB_NAME"]

    app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    db.init_app(app)
    alembic.init_app(app)
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    with app.app_context():
        db.create_all()
            

    @app.route("/hello")
    def hello_world():
        return "<p>Hello, World!</p>"
    
    @app.route("/user-by-username/<username>", methods=['POST', 'GET'])
    def user_by_username(username):
        searched_user = db.session.execute(db.select(user.User).filter_by(user_name=username)).scalar_one()
        return render_template("show_user.html", user=searched_user)
    
    return app
