from flask import Blueprint

mod = Blueprint('general', __name__)

from app.views import general