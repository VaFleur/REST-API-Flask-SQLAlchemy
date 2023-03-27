from flask import Blueprint
from controllers.department_controller import add_department, add_user_to_department, get_all_departments,\
    get_all_users_in_department, update_department, delete_department, delete_all_users_from_department,\
    delete_user_from_department

department_bp = Blueprint('department_bp', __name__)

# Add department
department_bp.route('/', methods=['POST'])(add_department)

# Add user to department
department_bp.route('/user', methods=['POST'])(add_user_to_department)

# Get all departments
department_bp.route('/', methods=['GET'])(get_all_departments)

# Get all users in department
department_bp.route('/<int:department_id>', methods=['GET'])(get_all_users_in_department)

# Update department
department_bp.route('/<int:department_id>', methods=['PUT'])(update_department)

# Delete department
department_bp.route('/<int:department_id>', methods=['DELETE'])(delete_department)

# Delete user from department
department_bp.route('/<int:department_id>/user/<int:user_id>', methods=['DELETE'])(delete_user_from_department)

# Delete all users from department
department_bp.route('/<int:department_id>/all', methods=['DELETE'])(delete_all_users_from_department)
