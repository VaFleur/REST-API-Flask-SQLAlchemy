from database.models import *
from typing import Optional
from datetime import datetime
from collections import defaultdict
from sqlalchemy.inspection import inspect

types_mapper = {
    str: "string",
    int: "integer",
    datetime: "string"
}


class ModelMapper:
    model_type_to_class = {}
    model_columns = defaultdict(dict)
    model_json_schema = defaultdict(dict)

    for class_ in Base.__subclasses__():
        model_type_to_class[class_.__tablename__] = class_

        json_schema = {
            "type": "object",
            "properties": {},
            "required": [],
            "additional_properties": False
        }

        for column in inspect(class_).column_attrs:
            model_columns[class_.__tablename__][column.key] = {
                "python_type": column.expression.type.python_type,
                "is_required": not column.expression.nullable
            }
            json_schema["properties"][column.key] = {
                "type": types_mapper.get(column.expression.type.python_type)
            }
            if column.key != "id" and not column.expression.nullable:
                json_schema["required"].append(column.key)

        model_json_schema[class_.__tablename__] = json_schema

    @classmethod
    def get_table(cls, model_type: str) -> Optional[Base]:
        return cls.model_type_to_class.get(model_type)

    @classmethod
    def get_columns(cls, model_type: str) -> Optional[dict]:
        return cls.model_columns.get(model_type)

    @classmethod
    def get_json_schema(cls, model_type: str) -> Optional[dict]:
        return cls.model_json_schema.get(model_type)
