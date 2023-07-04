from base.base_controller import BaseController
from flask import Request, Response


class ArticleController(BaseController):
    @classmethod
    def get_by_id(cls, request: Request) -> Response:
        return super(ArticleController, cls).get_by_id(request)

    @classmethod
    def get(cls, request: Request) -> Response:
        return super(ArticleController, cls).get(request)

    @classmethod
    def post(cls, request: Request) -> Response:
        return super(ArticleController, cls).post(request)

    @classmethod
    def put(cls, request: Request) -> Response:
        return super(ArticleController, cls).put(request)

    @classmethod
    def delete(cls, request: Request) -> Response:
        return super(ArticleController, cls).delete(request)
