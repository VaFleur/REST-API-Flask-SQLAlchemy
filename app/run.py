from application import app
from config import host, port, debug
import routes.users
import routes.emails
import routes.phones
import routes.departments

if __name__ == '__main__':
    app.run(debug=debug, port=port, host=host)
