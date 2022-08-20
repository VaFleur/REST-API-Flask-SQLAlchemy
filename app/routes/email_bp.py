from flask import request, Blueprint
from controllers import EmailController

email_bp = Blueprint('email_bp', __name__)
