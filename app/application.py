from flask import Flask
from routes import register_routes
from database import PGContextSession

__all__ = ["app"]

app = Flask(__name__)
# добавить middlewares

# добавить создание сессии

register_routes(app)
