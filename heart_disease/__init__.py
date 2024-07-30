from flask import Blueprint

heart_bp = Blueprint('heart', __name__, template_folder='templates', static_folder='static')

from . import views
