from flask import Flask
from routes import register_routes
from database.connection import PGContextSession
from middlewares import middleware_list

__all__ = ["app"]

app = Flask(__name__)

app.before_request_funcs = {"app": middleware_list}

#TODO потестить
with app.app_context():
    PGContextSession.setup(app)

register_routes(app)
