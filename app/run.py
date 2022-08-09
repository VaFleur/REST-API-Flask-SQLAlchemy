from application import app
from config import host, port, debug
import routes

if __name__ == '__main__':
    app.run(debug=debug, port=port, host=host)
