from database import PGContextSession
from flask import Response, Request
from application import app


@app.before_request
def session_middleware(request: Request, handler) -> Response:
    with PGContextSession as session:
        request.json["postgres_session"] = session
        response = handler(Request)
    return response
