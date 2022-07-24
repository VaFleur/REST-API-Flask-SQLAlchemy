from flask import request, jsonify
from werkzeug.security import generate_password_hash
from database.models import User, Phone, Department, Email
from database.session import session
from app import app



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

    for record in records:
        record_object = {
            'id': record.user_id,
            'username': record.username,
            'password': record.password,
            'first_name': record.first_name,
            'last_name': record.last_name,
            'phone': str(record.phone),
            'email': str(record.email),
            'department': str(record.department)
        }
        record_objects.append(record_object)
    return jsonify(record_objects)

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
            'phone': str(record.phone),
            'email': str(record.email),
            'department': str(record.department)
        }
        return jsonify(record_object)
    except:
        return jsonify({'Error': 'User does not exist'})

@app.route('/user/<int:id>', methods=['PUT'])
def update_user(id):
    try:
        record = session.query(User).get(id)

        # вторая ссылка из гугла "sqlalchemy how to update object" https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_updating_objects.htm
        new_record = request.json

        for key, value in new_record.items():
            if key == "username":
                record.username = value
            elif key == "first_name":
                record.first_name = value
            ... и так далее
            # в python3.10 для этого лучше использовать switch case (гугл в помощь)
            ##############################################################################
            # либо можно чуть сложнее:

            # проверяем что такое поле существует у нашей sqlalchemy модели
            if value in record.__dict__:
                # если существует, перезаписываем его
                setattr(record, value)
            # но пока лучше не выпендриваться с атрибутами класса и сделать через if else как в примере выше
            ##############################################################################

        session.add(record)
        session.commit()





        # record_object = {
        #     'username': record.username,
        #     'password': record.password,
        #     'first_name': record.first_name,
        #     'last_name': record.last_name,
        #     'phone': str(record.phone),
        #     'email': str(record.email),
        #     'department': str(record.department)
        # }
        #
        # new_record = request.json
        #
        # for key in record_object.keys():
        #     if key in new_record.keys():
        #         record_object[key] = new_record[key]
        #         if key == 'password':
        #             record_object[key] = generate_password_hash(new_record[key])
        #     else:
        #         print(f"Key {key} has not been found")
        # print(record_object)
        #
        # session.execute(
        #     update(User).
        #     where(User.user_id == id).
        #     values(username=record_object['username'],
        #            password=record_object['password'],
        #            first_name=record_object['first_name'],
        #            last_name=record_object['last_name'],
        #            phone=record_object['phone'],
        #            email=record_object['email'],
        #            department=record_object['department']
        #            )
        # )
        # session.commit()

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