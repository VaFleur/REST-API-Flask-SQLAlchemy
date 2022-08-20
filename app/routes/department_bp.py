from flask import request, Blueprint
from controllers import DepartmentController

department_bp = Blueprint('department_bp', __name__)
