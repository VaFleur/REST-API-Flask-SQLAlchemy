from datetime import datetime
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import Column, DateTime, Integer, ForeignKey, text


class MixinCRUD:
    system_fields = {
        "created_at", "updated_at", "deleted_at",
        "created_by", "updated_by", "deleted_by"
    }

    def label_created(self, user_id: int):
        setattr(self, "created_at", datetime.utcnow())
        setattr(self, "created_by", user_id)

    def label_updated(self, user_id: int):
        setattr(self, "updated_at", datetime.utcnow())
        setattr(self, "updated_by", user_id)

    def label_deleted(self, user_id):
        setattr(self, "deleted_at", datetime.utcnow())
        setattr(self, "deleted_by", user_id)

    @declared_attr
    def created_at(self):
        return Column(DateTime, nullable=True, server_default=text("now()"))

    @declared_attr
    def created_by(self):
        return Column(Integer, ForeignKey("user_table.id"), nullable=True)

    @declared_attr
    def updated_at(self):
        return Column(DateTime, nullable=True, server_default=text("now()"))

    @declared_attr
    def updated_by(self):
        return Column(Integer, ForeignKey("user_table.id"), nullable=True)

    @declared_attr
    def deleted_at(self):
        return Column(DateTime, nullable=True, server_default=text("now()"))

    @declared_attr
    def deleted_by(self):
        return Column(Integer, ForeignKey("user_table.id"), nullable=True)

