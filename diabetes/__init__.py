from flask import Blueprint

diabetes_bp = Blueprint('diabetes', __name__, template_folder='templates', static_folder='static')

from . import views
