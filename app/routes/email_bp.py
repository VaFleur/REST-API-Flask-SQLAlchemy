from flask import Blueprint
from controllers.EmailController import add_email, delete_all_emails, delete_email, get_all_emails,\
    get_emails_for_user, update_email

email_bp = Blueprint('email_bp', __name__)

# Add email for user
email_bp.route('/', methods=['POST'])(add_email)

# Delete all emails for user
email_bp.route('/user/<int:user_id>', methods=['DELETE'])(delete_all_emails)

# Delete email using its ID
email_bp.route('/<int:user_id>', methods=['DELETE'])(delete_email)

# Get all emails
email_bp.route('/', methods=['GET'])(get_all_emails)

# Get user's emails
email_bp.route('/<int:user_id>', methods=['GET'])(get_emails_for_user)

# Update email
email_bp.route('/<int:email_id>', methods=['PUT'])(update_email)
