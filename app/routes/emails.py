from flask import request, jsonify
from application import app
from database.models import Email, User
from database.session import session


@app.route('/email/<int:id>', methods=['POST'])
def add_email(id):
    try:
        new_record = request.json

        record_email = Email(
            email=new_record['email'],
            user_id=id
        )

        session.add(record_email)
        session.commit()

        return jsonify({"Success": f"Email for user id{id} has been added"})
    except Exception as e:
        return jsonify({"Error": f"{e}"})


@app.route('/email/', methods=['GET'])
def get_emails():
    try:
        record_objects = []
        records = session.query(Email).all()

        for record in records:
            record_object = {
                'id': record.user_id,
                'email': record.email
            }
            record_objects.append(record_object)

        return jsonify(record_objects)
    except Exception as e:
        return jsonify({"Error": f"{e}"})


@app.route('/email/<int:id>', methods=['GET'])
def get_email(id):
    try:
        record = session.query(Email).filter_by(user_id=id).all()
        emails = [line.email for line in record]

        record_object = {
            'id': id,
            'emails': emails
        }

        return jsonify(record_object)
    except Exception as e:
        return jsonify({"Error": f"{e}"})


@app.route('/email/<int:id>', methods=['PUT'])
def update_email(id):
    try:
        record = session.query(Email).get(id)
        new_record = request.json

        for key, value in new_record.items():
            match key:
                case "email":
                    record.email = value

        session.add(record)
        session.commit()

        return jsonify({"Success": f"Email for user id{id} has been updated"})
    except Exception as e:
        return jsonify({"Error": f"{e}"})


@app.route('/email/<int:id>', methods=['DELETE'])
def delete_email(id):
    try:
        record = session.query(Email).filter_by(user_id=id).all()

        session.delete(record)
        session.commit()

        return jsonify({"Success": f"Email for user id{id} has been deleted"})
    except Exception as e:
        return jsonify({"Error": f"{e}"})
