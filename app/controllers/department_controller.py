from base import BaseController
from flask import Request, Response


class DepartmentController(BaseController):
    @classmethod
    def get_by_id(cls, request: Request) -> Response:
        return super(DepartmentController, cls).get_by_id(request)

    @classmethod
    def get(cls, request: Request) -> Response:
        return super(DepartmentController, cls).get(request)

    @classmethod
    def post(cls, request: Request) -> Response:
        return super(DepartmentController, cls).post(request)

    @classmethod
    def put(cls, request: Request) -> Response:
        return super(DepartmentController, cls).put(request)

    @classmethod
    def delete(cls, request: Request) -> Response:
        return super(DepartmentController, cls).delete(request)
