from database.connection import connect_to_database
from database.models import User
from werkzeug.security import generate_password_hash
from flask import request, jsonify

session = connect_to_database()


def add_user():
    try:
        data = request.json
        user = User()
        user.username = data['username']
        user.password = generate_password_hash(data['password'])
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.phone = data['phone']
        session.add(user)
        session.commit()
        return jsonify({"Success": f"User id{user.id} has been added"})
    except Exception as e:
        return jsonify({"Error": f"{e}"})
    finally:
        session.close()


def delete_user(user_id):
    try:
        record = session.query(User).filter_by(id=user_id).one()
        session.delete(record)
        session.commit()
        return jsonify({"Success": f"User id{user_id} has been deleted"})
    except Exception as e:
        return jsonify({"Error": f"{e}"})
    finally:
        session.close()


def update_user(user_id):
    try:
        data = request.json
        record = session.query(User).filter_by(id=user_id).one()
        for key, value in data.items():
            match key:
                case "username":
                    record.username = value
                case "password":
                    record.password = generate_password_hash(value)
                case "first_name":
                    record.first_name = value
                case "last_name":
                    record.last_name = value
                case "phone":
                    record.phone = value
        session.add(record)
        session.commit()
        return jsonify({"Success": f"User id{user_id} has been updated"})
    except Exception as e:
        return jsonify({"Error": f"{e}"})
    finally:
        session.close()


def make_user_dict(record):
    user = {
        'id': record.id,
        'username': record.username,
        'password': record.password,
        'first_name': record.first_name,
        'last_name': record.last_name,
        'phone': record.phone
    }
    return user


def convert_user_results(results):
    users = []
    for record in results:
        user = make_user_dict(record)
        users.append(user)
    return users


def get_users():
    try:
        result = session.query(User).all()
        users = convert_user_results(result)
        return jsonify(users)
    except Exception as e:
        return jsonify({"Error": f"{e}"})
    finally:
        session.close()


def get_user(user_id):
    try:
        result = session.query(User).filter_by(id=user_id).one()
        user = make_user_dict(result)
        return user
    except Exception as e:
        return jsonify({"Error": f"{e}"})
    finally:
        session.close()
