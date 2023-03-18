from flask import Blueprint

index = Blueprint('index', __name__)

@index.route('/overview')
def overview():
    return 'Overview'