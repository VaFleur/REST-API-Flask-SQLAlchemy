from base.request_data import RequestData
from utils.validation_utils import ValidationUtils


class BaseValidator:
    @classmethod
    def get_by_id(cls, request_data: RequestData):
        ValidationUtils.check_entity_type_correct(request_data)
        ValidationUtils.check_entity_exists_by_id(request_data)

    @classmethod
    def get(cls, request_data: RequestData):
        ValidationUtils.check_entity_type_correct(request_data)

    @classmethod
    def post(cls, request_data: RequestData):
        ValidationUtils.check_entity_type_correct(request_data)
        ValidationUtils.check_create_json_schema(request_data)

    @classmethod
    def put(cls, request_data: RequestData):
        ValidationUtils.check_entity_type_correct(request_data)
        ValidationUtils.check_entity_exists_by_id(request_data)
        ValidationUtils.check_update_json_schema(request_data)

    @classmethod
    def delete(cls, request_data: RequestData):
        ValidationUtils.check_entity_type_correct(request_data)
        ValidationUtils.check_entity_exists_by_id(request_data)
