from flask import Blueprint, render_template, make_response
from flask_login import login_required


overview = Blueprint('overview', __name__)


@overview.route('/overview')
@login_required
def overview_page():
    
    response = make_response(render_template('overview.html'))
    
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'    
    
    response.headers['X-Content-Type-Options'] = 'nosniff'
    
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    
    return response
