import base64
from database import User, DatabaseAgent
from sqlalchemy.orm import Session
from flask import Response, Request
from utils import ExecutionException
from application import app


def _get_user(nickname: str, password: str, request: Request) -> User:
    session: Session = request.form["postgres_session"]
    filters = (
        User.nickname == nickname,
        User.password == password
    )
    return DatabaseAgent.get_one(session, User, filters)


def _check_auth(cls, request: Request) -> bool:
    authorization = request.headers.get("Authorization")
    if authorization and authorization.lower().startswith("basic "):
        credentials = base64.b64decode(authorization[6:]).decode("utf-8")
        nickname, password = credentials.split(":")
        user: User = cls._get_user(nickname, password, request)
        if user:
            request.form["user_id"] = user.id
            return True
    return False


@app.before_request
def auth_middleware(cls, request: Request, handler) -> Response:
    if cls._check_auth(request):
        return handler(request)
    message = "Авторизируйтесь через Basic Auth"
    raise ExecutionException("auth-error", message, 401)


