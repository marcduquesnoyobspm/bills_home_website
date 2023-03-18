from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import current_user, login_user, login_required


index = Blueprint('index', __name__)


@index.route('/')
def welcome():
    return render_template('welcome.html')


@index.route('/overview')
@login_required
def overview():
    return render_template('overview.html')