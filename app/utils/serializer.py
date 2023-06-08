from typing import Iterable, Tuple, Optional
from collections import defaultdict
from database.models import Base as SQLAlchemyBase
from database.mapper import ModelMapper
from datetime import datetime
from flask import Response, jsonify


class ResponseSerializer:
    def __init__(self):
        self._data: defaultdict = None
        self._included: defaultdict = defaultdict(dict)
        self._is_collection: bool = False

    @staticmethod
    def _serialize_object(entity: SQLAlchemyBase) -> dict:
        data = {
            'id': getattr(entity, 'id', None),
            'model_type': getattr(entity, '__tablename__', None),
            'attributes': {}
        }
        attrs = ModelMapper.get_columns(getattr(entity, "__tablename__", None))
        hidden_attrs = getattr(entity, "_hidden", None)
        if attrs:
            for key, _ in attrs.items():
                if key in hidden_attrs:
                    continue
                value = getattr(entity, key, None)
                if isinstance(value, datetime):
                    data["attributes"][key] = value.strftime('%Y-%m-%d %H:%M:%S')
                elif value is None:
                    data["attributes"][key] = value
                else:
                    data["attributes"][key] = str(value)
        return data

    @staticmethod
    def _get_entity_params(entity: SQLAlchemyBase) -> Tuple[Optional[int], Optional[str]]:
        model_type = getattr(entity, "__tablename__", None)
        entity_id = getattr(entity, "id", None)
        return entity_id, model_type

    def serialize_object(self, entity: SQLAlchemyBase) -> "ResponseSerializer":
        self._is_collection = False
        if entity and isinstance(entity, SQLAlchemyBase):
            self._data = self.serialize_object(entity)
        else:
            self._data = {
                "id": None,
                "model_type": None,
                "attributes": {}
            }
        return self

    def serialize_collection(self, entities: Iterable[SQLAlchemyBase]) -> "ResponseSerializer":
        self._is_collection = True
        self._data = defaultdict(dict)
        for entity in entities:
            if entity and isinstance(entity, SQLAlchemyBase):
                entity_id, model_type = self._get_entity_params(entity)
                self._data[model_type][entity_id] = entity
        return self

    def append_object_in_included(self, entity: SQLAlchemyBase) -> "ResponseSerializer":
        if entity and isinstance(entity, SQLAlchemyBase):
            entity_id, model_type = self._get_entity_params(entity)
            self._included[model_type][entity_id] = entity
        return self

    def append_collection_in_included(self, entities: Iterable[SQLAlchemyBase]) -> "ResponseSerializer":
        for entity in entities:
            if entity and isinstance(entity, SQLAlchemyBase):
                entity_id, model_type = self._get_entity_params(entity)
                self._included[model_type][entity_id] = entity
        return self

    @property
    def response(self) -> Response:
        if self._is_collection:
            data = []
            for model_type, entities in self._data.items():
                data = []
                for entity_id, entity in entities.items():
                    data.append(self._serialize_object(entity))
        else:
            data = self._data

        included = defaultdict(list)
        for model_type, entities in self._included.items():
            for entity_id, entity in entities.items():
                included[model_type].append(self._serialize_object(entity))

        result = {
            "data": data,
            "included": included
        }
        return jsonify(result)
