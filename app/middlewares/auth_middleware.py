import base64
from database import User, DatabaseAgent
from sqlalchemy.orm import Session
from werkzeug import Response, Request
from utils import ExecutionException


class AuthMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        # Говнокодить сюда
        request = Request(environ)
        response = Response(start_response)
        # Конец говнокода
        return self.app(environ, start_response)

    @staticmethod
    def _get_user(nickname: str, password: str, request: Request) -> User:
        session: Session = request.form["postgres_session"]
        filters = (
            User.nickname == nickname,
            User.password == password
        )
        return DatabaseAgent.get_one(session, User, filters)

    @classmethod
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

    @classmethod
    def _auth_middleware(cls, request: Request, handler) -> Response:
        if cls._check_auth(request):
            return handler(request)
        message = "Авторизируйтесь через Basic Auth"
        raise ExecutionException("auth-error", message, 401)


