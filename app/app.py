from routes import app
from config import host, port, debug

if __name__ == '__main__':
    app.run(debug = debug, port = port, host = host)