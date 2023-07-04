from validators.user_validator import UserValidator
from flask import Response, Request
from base.request_data import RequestData
from base.base_controller import BaseController
from business_models.users_business_model import UserBusinessModel
from utils.serializer import ResponseSerializer


class UserController(BaseController):
    @classmethod
    def get_by_id(cls, request: Request) -> Response:
        return super(UserController, cls).get_by_id(request)

    @classmethod
    def get(cls, request: Request) -> Response:
        return super(UserController, cls).get(request)

    @classmethod
    def post(cls, request: Request) -> Response:
        request_data = RequestData.create(request)
        UserValidator.post(request_data)
        bm = UserBusinessModel(request_data)
        entity = bm.create()
        return ResponseSerializer().serialize_object(entity).response

    @classmethod
    def put(cls, request: Request) -> Response:
        request_data = RequestData.create(request)
        UserValidator.put(request_data)
        bm = UserBusinessModel(request_data)
        entity = bm.update()
        return ResponseSerializer().serialize_object(entity).response

    @classmethod
    def delete(cls, request: Request) -> Response:
        return super(UserController, cls).delete(request)
