from base import RequestData, BaseValidator, BaseBusinessModel
from utils import ResponseSerializer, ExecutionException
from flask import Request, Response


class BaseController:
    @staticmethod
    def _raise_not_implement() -> None:
        raise ExecutionException(
            error="not-implemented",
            message="HTTP method not implemented for entity",
            http_code=205
        )

    @classmethod
    def get_by_id(cls, request: Request) -> Response:
        request_data = RequestData.create(request)
        BaseValidator.get_by_id(request_data)
        bm = BaseBusinessModel(request_data)
        entity = bm.get_by_id()
        return ResponseSerializer().serialize_object(entity).response

    @classmethod
    def get(cls, request: Request) -> Response:
        request_data = RequestData.create(request)
        BaseValidator.get(request_data)
        bm = BaseBusinessModel(request_data)
        entities = bm.search()
        return ResponseSerializer().serialize_collection(entities).response

    @classmethod
    def post(cls, request: Request) -> Response:
        request_data = RequestData.create(request)
        BaseValidator.post(request_data)
        bm = BaseBusinessModel(request_data)
        entity = bm.create()
        return ResponseSerializer().serialize_object(entity).response

    @classmethod
    def put(cls, request: Request) -> Response:
        request_data = RequestData.create(request)
        BaseValidator.put(request_data)
        bm = BaseBusinessModel(request_data)
        entity = bm.update()
        return ResponseSerializer().serialize_object(entity).response

    @classmethod
    def delete(cls, request: Request) -> Response:
        request_data = RequestData.create(request)
        BaseValidator.delete(request_data)
        bm = BaseBusinessModel(request_data)
        entity = bm.delete()
        return ResponseSerializer().serialize_object(entity).response

    @classmethod
    def patch(cls, request: Request) -> None:
        cls._raise_not_implement()
