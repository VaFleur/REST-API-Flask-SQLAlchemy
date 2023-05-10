from flask import Flask
from routes import register_routes
from database import PGContextSession
from middlewares import middleware_list

__all__ = ["app"]

app = Flask(__name__)

app.before_request_funcs = {"app": middleware_list}

app.before_first_request(PGContextSession.setup)

register_routes(app)
