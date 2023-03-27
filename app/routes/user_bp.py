from flask import Blueprint
from controllers.user_controller import add_user, get_user, get_ausers, update_user, delete_user

user_bp = Blueprint('user_bp', __name__)

# Add user
user_bp.route('/', methods=['POST'])(add_user)

# Get all users
user_bp.route('/', methods=['GET'])(get_users)

# Get user by ID
user_bp.route('/<int:user_id>', methods=['GET'])(get_user)

# Update user
user_bp.route('/<int:user_id>', methods=['PUT'])(update_user)

# Delete user
user_bp.route('/<int:user_id>', methods=['DELETE'])(delete_user)
