from database.models import Base
from sqlalchemy import func, select
from typing import Iterable
from sqlalchemy.sql.expression import BinaryExpression, Select
from sqlalchemy.orm import Session


class DatabaseAgent:
    @staticmethod
    def add_base_filters(statement: Select, entity_model: Base) -> Select:
        return statement.filter(entity_model.deleted_at.is_(None), entity_model.deleted_by.is_(None))

    @classmethod
    def count(cls, session: Session, entity_model: Base, filters: Iterable[BinaryExpression] = None) -> int:
        count = func.count(entity_model.id)
        count = cls.add_base_filters(count, entity_model)

        if filters:
            for criterion in filters:
                count = count.filter(criterion)

        result = session.execute(select(count))
        return result.scalar()

    @classmethod
    def get_one(cls, session: Session, entity_model: Base, filters: Iterable[BinaryExpression] = None) -> Base:
        statement = select(entity_model)
        statement = cls.add_base_filters(statement, entity_model)

        if filters:
            for criterion in filters:
                statement = statement.filter(criterion)

        result = session.execute(statement)
        return result.scalar()

    @classmethod
    def get_all(cls, session: Session, entity_model: Base, filters: Iterable[BinaryExpression] = None) -> Iterable[Base]:
        statement = select(entity_model)
        statement = cls.add_base_filters(statement, entity_model)

        if filters:
            for criterion in filters:
                statement = statement.filter(criterion)

        result = session.execute(statement)
        return result.scalars()

    @classmethod
    def get_by_id(cls, session: Session, entity_model: Base, entity_id: int) -> Base:
        statement = select(entity_model).filter(entity_model.id == entity_id)
        statement = cls.add_base_filters(statement, entity_model)

        result = session.execute(statement)
        return result.scalar()
