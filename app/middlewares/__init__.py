from .auth_middleware import auth_middleware
from .session_middleware import session_middleware
from .error_handler_middleware import error_handler_middleware


middleware_list = [
    auth_middleware,
    session_middleware,
    error_handler_middleware
]
