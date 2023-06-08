from database.models import Base
from database.mapper import ModelMapper
from typing import Optional
from flask import Request
from sqlalchemy.orm import Session
from utils.custom_exception import ExecutionException


class RequestData:
    def __init__(self,
                 headers: dict,
                 request: Request,
                 user_id: Optional[int],
                 payload: Optional[dict],
                 params: Optional[dict],
                 pg_session: Session,
                 entity_id: Optional[int],
                 entity_type: Optional[str],
                 entity_model: Optional[Base]
                 ):
        self._request = request
        self._headers: dict = headers
        self._params: Optional[dict] = params
        self._payload: Optional[dict] = payload

        self._user_id: Optional[int] = user_id
        self._entity_id: Optional[int] = entity_id
        self._entity_type: Optional[str] = entity_type
        self._entity_model: Optional[Base] = entity_model
        self._pg_session: Session = pg_session

    @property
    def request(self) -> Request:
        return self._request

    @property
    def pg_session(self) -> Session:
        return self._pg_session

    @property
    def headers(self) -> dict:
        return self._headers

    @property
    def user_id(self) -> Optional[int]:
        return self._user_id

    @property
    def entity_id(self) -> Optional[int]:
        return self._entity_id

    @property
    def entity_type(self) -> Optional[str]:
        return self._entity_type

    @property
    def entity_model(self) -> Optional[Base]:
        return self._entity_model

    @property
    def payload(self) -> Optional[dict]:
        return self._payload

    @property
    def params(self) -> Optional[dict]:
        return self._params

    @staticmethod
    def _get_entity_type(request: Request) -> tuple[Optional[str], Optional[Base]]:
        """Потестить, возможна ошибка"""
        entity_type = request.form.get("entity_type")
        if entity_type:
            return entity_type, ModelMapper.get_table(entity_type)

        for part in request.url.split("/"):
            if part and ModelMapper.get_table(part):
                return part, ModelMapper.get_table(part)

        return None, None

    @staticmethod
    def _get_body(request: Request) -> Optional[dict]:
        """Потестить, возможна ошибка"""
        if request.form:
            if request.content_type == "application/json":
                return request.json
            else:
                raise ExecutionException(
                    error="content-type-error",
                    message="body content_type must be application/json",
                    http_code=415
                )
        return None

    @classmethod
    def create(cls, request: Request) -> "RequestData":
        """Потестить, возможна ошибка"""
        body = cls._get_body(request)
        entity_id: str = request.form.get("id")
        entity_type, entity_model = cls._get_entity_type(request)

        return cls(
            payload=body,
            request=request,
            entity_type=entity_type,
            entity_model=entity_model,
            user_id=request.form.get("user_id"),
            params=dict(request.args),
            headers=dict(request.headers),
            pg_session=request.form.get("postgres_session"),
            entity_id=entity_id if entity_id and entity_id.isdigit() else None
        )
