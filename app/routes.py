from flask import request, jsonify, Flask
from werkzeug.security import generate_password_hash
from sqlalchemy.orm import sessionmaker
from model import User, Phone, Department, Email, engine

app = Flask(__name__)
Session = sessionmaker(bind=engine)
session = Session()

@app.route('/user/', methods=['POST'])
def add_user():
    try:
        record_user = User(
            username=request.json['username'],
            password=generate_password_hash(request.json['password']),
            first_name=request.json['first_name'],
            last_name=request.json['last_name'],
        )
        record_phone = Phone(phone=request.json['phone'])
        record_email = Email(email=request.json['email'])
        record_department = Department(department=request.json['department'])

        session.add_all([record_user, record_phone, record_email, record_department])
        session.commit()
        return jsonify({"Success": f"User idXX has been added"})
    except:
        return jsonify({"Error": f"User idXX has not been added"})

@app.route('/user/', methods=['GET'])
def get_users():
    record_objects = []
    records = session.query(User).all()

    for record in records:
        record_object = {
            'id': record.id,
            'username': record.username,
            'password': record.password,
            'email': record.email,
            'first_name': record.first_name,
            'last_name': record.last_name
        }
        record_objects.append(record_object)
    return jsonify(record_objects)

@app.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    record = session.query(User).get(id)

    record_object = {
        'id': record.id,
        'username': record.username,
        'password': record.password,
        'email': record.email,
        'first_name': record.first_name,
        'last_name': record.last_name
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