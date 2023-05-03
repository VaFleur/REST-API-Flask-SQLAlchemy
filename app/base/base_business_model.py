from typing import Iterable
from base import RequestData
from database import Base, DatabaseAgent
from sqlalchemy.orm import Session


class BaseBusinessModel:
    def __init__(self, request_data: RequestData):
        self._request_data: RequestData = request_data
        self._pg_session: Session = request_data.pg_session

    @property
    def request_data(self) -> RequestData:
        return self._request_data

    @property
    def session(self) -> Session:
        return self._pg_session

    def get_by_id(self) -> Base:
        entity = DatabaseAgent.get_by_id(
            session=self.session,
            entity_id=self.request_data.entity_id,
            entity_model=self.request_data.entity_model
        )
        return entity

    def search(self) -> Iterable[Base]:
        entities = DatabaseAgent.get_all(
            session=self.session,
            entity_model=self.request_data.entity_model
        )
        return entities

    def create(self) -> Base:
        entity = self.request_data.entity_model()
        for attribute, value in self.request_data.payload["data"]["attributes"].items():
            if attribute != "id" and attribute not in entity.system_fields:
                setattr(entity, attribute, value)
        entity.label_created(self.request_data.user_id)
        self.session.add(entity)
        self.session.commit()
        self.session.refresh(entity)
        return entity

    def update(self) -> Base:
        entity = DatabaseAgent.get_by_id(
            session=self.session,
            entity_id=self.request_data.entity_id,
            entity_model=self.request_data.entity_model
        )
        for attribute, value in self.request_data.payload["data"]["attributes"].items():
            if attribute != "id" and attribute not in entity.system_fields:
                setattr(entity, attribute, value)
        entity.label_updated(self.request_data.user_id)
        self.session.add(entity)
        self.session.commit()
        self.session.refresh(entity)
        return entity

    def delete(self) -> Base:
        entity = DatabaseAgent.get_by_id(
            session=self.session,
            entity_id=self.request_data.entity_id,
            entity_model=self.request_data.entity_model
        )
        entity.label_deleted(self.request_data.user_id)
        self.session.add(entity)
        self.session.commit()
        self.session.refresh(entity)
        return entity
