from base.request_data import RequestData
from base.base_validator import BaseValidator
from utils.validation_utils import ValidationUtils


class UserValidator(BaseValidator):
    @classmethod
    def post(cls, request_data: RequestData):
        super(UserValidator, cls).post(request_data)

        password = request_data.payload["data"]["attributes"]["password"]
        if len(password) < 8:
            ValidationUtils.raise_validation_error("Password must contain 8 characters or more")

    @classmethod
    def put(cls, request_data: RequestData):
        super(UserValidator, cls).put(request_data)

        password = request_data.payload["data"]["attributes"].get("password")
        if password and len(password) < 8:
            ValidationUtils.raise_validation_error("Password must contain 8 characters or more")
