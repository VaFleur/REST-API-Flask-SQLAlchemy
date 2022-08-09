from flask import request, jsonify
from application import app
from database.models import Department, UserDepartment
from database.session import session


@app.route('/department/', methods=['POST'])
def add_department():
    try:
        new_record = request.json

        record_department = Department(
            department=new_record['department']
        )

        session.add(record_department)
        session.commit()

        return jsonify({"Success": f"Department id{record_department.department_id} has been added"})
    except Exception as e:
        return jsonify({"Error": f"{e}"})


@app.route('/department/add_user_to_dpt/', methods=['POST'])
def add_user_to_dpt():
    try:
        new_record = request.json

        record_user_to_dpt = UserDepartment(
            user_id=new_record["user_id"],
            department_id=new_record["department_id"]
        )

        session.add(record_user_to_dpt)
        session.commit()

        return jsonify({"Success": f"User has been added to department"})
    except Exception as e:
        return jsonify({"Error": f"{e}"})


@app.route('/department/', methods=['GET'])
def get_departments():
    try:
        record_objects = []
        records = session.query(Department).all()

        for record in records:
            record_object = {
                'department_id': record.department_id,
                'department': record.department
            }
            record_objects.append(record_object)

        return jsonify(record_objects)
    except Exception as e:
        return jsonify({"Error": f"{e}"})


@app.route('/department/<int:id>', methods=['GET'])
def get_users_in_department(id):
    try:
        record = session.query(UserDepartment).filter_by(department_id=id).all()
        user_ids = [line.user_id for line in record]

        record_object = {
            'id': id,
            'department': id,
            'user ids': user_ids
        }

        return jsonify(record_object)
    except Exception as e:
        return jsonify({"Error": f"{e}"})


@app.route('/department/<int:id>', methods=['PUT'])
def update_department(id):
    try:
        record = session.query(Department).get(id)
        new_record = request.json

        for key, value in new_record.items():
            match key:
                case "department":
                    record.department = value

        session.add(record)
        session.commit()

        return jsonify({"Success": f"Department id{id} has been updated"})
    except Exception as e:
        return jsonify({"Error": f"{e}"})


@app.route('/department/<int:id>', methods=['DELETE'])
def delete_department(id):
    try:
        record = session.query(Department).filter(Department.user_id == id)

        session.delete(record)
        session.commit()

        return jsonify({"Success": f"Department for user id{id} has been deleted"})
    except Exception as e:
        return jsonify({"Error": f"{e}"})