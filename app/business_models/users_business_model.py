from database import User
from base import BaseBusinessModel


class UserBusinessModel(BaseBusinessModel):
    def create(self) -> User:
        password = self.request_data.payload["data"]["attributes"]["password"]
        hash_ = User.get_password_hash(password)
        self.request_data.payload["data"]["attributes"]["password"] = hash_
        return super(UserBusinessModel, self).create()

    def update(self) -> User:
        password = self.request_data.payload["data"]["attributes"]["password"]
        if password:
            hash_ = User.get_password_hash(password)
            self.request_data.payload["data"]["attributes"]["password"] = hash_
        return super(UserBusinessModel, self).update()
