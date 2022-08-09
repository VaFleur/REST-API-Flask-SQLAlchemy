from flask import request, jsonify
from werkzeug.security import generate_password_hash
from application import app
from database.models import User
from database.session import session


@app.route('/user/', methods=['POST'])
def add_user():
    try:
        new_record = request.json

        record_user = User(
            username=new_record['username'],
            password=generate_password_hash(new_record['password']),
            first_name=new_record['first_name'],
            last_name=new_record['last_name'],
            phone=new_record['phone']
        )

        session.add(record_user)
        session.commit()

        return jsonify({"Success": f"User id{record_user.user_id} has been added"})
    except Exception as e:
        return jsonify({"Error": f"{e}"})


@app.route('/user/', methods=['GET'])
def get_users():
    try:
        record_objects = []
        records = session.query(User).all()

        for record in records:
            record_object = {
                'id': record.user_id,
                'username': record.username,
                'password': record.password,
                'first_name': record.first_name,
                'last_name': record.last_name,
                'phone': record.phone
            }
            record_objects.append(record_object)

        return jsonify(record_objects)
    except Exception as e:
        return jsonify({"Error": f"{e}"})


@app.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    try:
        record = session.query(User).get(id)

        record_object = {
            'id': record.user_id,
            'username': record.username,
            'password': record.password,
            'first_name': record.first_name,
            'last_name': record.last_name,
            'phone': record.phone
        }

        return jsonify(record_object)
    except Exception as e:
        return jsonify({"Error": f"{e}"})


@app.route('/user/<int:id>', methods=['PUT'])
def update_user(id):
    try:
        record = session.query(User).get(id)
        new_record = request.json

        for key, value in new_record.items():
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

        return jsonify({"Success": f"User id{id} has been updated"})
    except Exception as e:
        return jsonify({"Error": f"{e}"})


@app.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    try:
        record = session.query(User).get(id)

        session.delete(record)
        session.commit()

        return jsonify({"Success": f"User id{id} has been deleted"})
    except Exception as e:
        return jsonify({"Error": f"{e}"})
