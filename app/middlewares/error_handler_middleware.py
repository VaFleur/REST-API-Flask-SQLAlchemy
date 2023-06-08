from logger import logger
from utils.custom_exception import ExecutionException
from flask import Response, Request, jsonify


def error_handler_middleware(request: Request, handler) -> Response:
    try:
        return handler(request)
    except ExecutionException as e:
        return jsonify(
            status=e.http_code,
            data={"error": e.error, "message": e.message}
        )
    except BaseException as e:
        logger.error(e, exc_info=True)
        return jsonify(
            status=500,
            data={"error": f"{e.__class__.__name__}", "message": str(e)}
        )
