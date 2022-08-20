from application import app
from config import host, port, debug
from routes.user_bp import user_bp
from routes.email_bp import email_bp
from routes.department_bp import department_bp

# CRUD path for users
app.register_blueprint(user_bp, url_prefix='/users')

# CRUD path for emails
app.register_blueprint(email_bp, url_prefix='/emails')

# CRUD path for departments
app.register_blueprint(department_bp, url_prefix='/departments')

if __name__ == '__main__':
    app.run(debug=debug, port=port, host=host)
