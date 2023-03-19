from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import current_user, login_user, login_required


welcome = Blueprint('welcome', __name__)


@welcome.route('/')
def welcome_page():
    return render_template('welcome.html')