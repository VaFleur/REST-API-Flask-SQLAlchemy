from flask import request, jsonify
from werkzeug.security import generate_password_hash
from sqlalchemy.orm import sessionmaker
from models import User, Phone, Department, Email, engine
from app import app

Session = sessionmaker(bind=engine)
session = Session()

@app.route('/user/', methods=['POST'])
def add_user():
    try:
        record_user = User(
            username=request.json['username'],
            password=generate_password_hash(request.json['password']),
            first_name=request.json['first_name'],
            last_name=request.json['last_name']
        )

        session.add(record_user)
        session.commit()

        record_phone = Phone(
            phone=request.json['phone'],
            user_id=record_user.user_id
        )
        record_email = Email(
            email=request.json['email'],
            user_id=record_user.user_id
        )
        record_department = Department(
            department=request.json['department'],
            user_id=record_user.user_id
        )

        session.add_all([record_phone, record_email, record_department])
        session.commit()
        return jsonify({"Success": f"User id{record_user.user_id} has been added"})
    except:
        return jsonify({"Error": f"User has not been added"})

@app.route('/user/', methods=['GET'])
def get_users():
    record_objects = []
    records = session.query(User).all()

    for record_user in records:
        record_object = {
        'id': record_user.user_id,
        'username': record_user.username,
        'password': record_user.password,
        'first_name': record_user.first_name,
        'last_name': record_user.last_name,
        'phone': str(record_user.phone),
        'email': str(record_user.email),
        'department': str(record_user.department)
    }
        record_objects.append(record_object)
    return jsonify(record_objects)

@app.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    record_user = session.query(User).get(id)

    record_object = {
        'id': record_user.user_id,
        'username': record_user.username,
        'password': record_user.password,
        'first_name': record_user.first_name,
        'last_name': record_user.last_name,
        'phone': str(record_user.phone),
        'email': str(record_user.email),
        'department': str(record_user.department)
    }
    return jsonify(record_object)

@app.route('/user/<int:id>', methods=['PUT'])
def update_user(id):
    try:
        record = session.query(User).get(id)

        record.username = request.json['username']
        record.password = generate_password_hash(request.json['password'])
        record.email = request.json['email']
        record.first_name = request.json['first_name']
        record.last_name = request.json['last_name']

        session.add(record)
        session.commit()
        return jsonify({"Success": f"User id{id} has been updated"})
    except:
        return jsonify({"Error": f"User id{id} has not been updated"})

@app.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    try:
        record = session.query(User).get(id)

        session.delete(record)
        session.commit()
        return jsonify({"Success": f"User id{id} has been deleted"})
    except:
        return jsonify({"Error": f"User id{id} has not been deleted"})