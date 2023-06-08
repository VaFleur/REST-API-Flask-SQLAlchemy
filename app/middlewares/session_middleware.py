from database.connection import PGContextSession
from flask import Response, Request


def session_middleware(request: Request, handler) -> Response:
    with PGContextSession as session:
        request.json["postgres_session"] = session
        response = handler(Request)
    return response
