from database.connection import connect_to_database
from database.models import User
from werkzeug.security import generate_password_hash
from database.serializers import serialize_user


def add_user(user_data: dict) -> User:
    session = connect_to_database()

    try:
        user = User()
        user.username = user_data['username']
        user.password = generate_password_hash(user_data['password'])
        user.first_name = user_data['first_name']
        user.last_name = user_data['last_name']
        user.phone = user_data['phone']
        session.add(user)
        session.commit()
        return user
    finally:
        session.close()


def delete_user(user_id: int) -> None:
    session = connect_to_database()

    try:
        record = session.query(User).filter_by(id=user_id).one()
        session.delete(record)
        session.commit()
    finally:
        session.close()


def update_user(user_data: dict, user_id: int) -> User:
    session = connect_to_database()

    try:
        user = session.query(User).filter_by(id=user_id).one()
        for key, value in user_data.items():
            match key:
                case "username":
                    user.username = value
                case "password":
                    user.password = generate_password_hash(value)
                case "first_name":
                    user.first_name = value
                case "last_name":
                    user.last_name = value
                case "phone":
                    user.phone = value

        session.add(user)
        session.commit()
        return user
    finally:
        session.close()


def get_all_users() -> list:
    session = connect_to_database()

    try:
        users = session.query(User).all()
        user_list = serialize_user(users)
        return user_list
    finally:
        session.close()


def get_user(user_id: int) -> list:
    session = connect_to_database()

    try:
        users = session.query(User).filter_by(id=user_id).one()
        user_list = serialize_user(users)
        return user_list
    finally:
        session.close()