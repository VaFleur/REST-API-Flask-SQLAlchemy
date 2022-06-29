from flask import Flask
from config import host, port, debug

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug = debug, port = port, host = host)