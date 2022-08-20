from flask import request, Blueprint
from controllers.UserController import add_user, get_user, get_users, update_user, delete_user

user_bp = Blueprint('user_bp', __name__)

# Add user
user_bp.route('/', methods=['POST'])(add_user(data=request.json))

# Get all users
user_bp.route('/', methods=['GET'])(get_users())

# Get user by ID
user_bp.route('/<int:user_id>', methods=['GET'])(get_user(user_id=user_id))

# Update user
user_bp.route('/<int:user_id>', methods=['PUT'])(update_user(user_id=user_id, data=request.json))

# Delete user
user_bp.route('/<int:user_id>', methods=['DELETE'])(delete_user(user_id=user_id))
