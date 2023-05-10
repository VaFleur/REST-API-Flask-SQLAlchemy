from application import app
from logger import logger
from utils import ExecutionException
from flask import Response, Request, jsonify


@app.before_request
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
