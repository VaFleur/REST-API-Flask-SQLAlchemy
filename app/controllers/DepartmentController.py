from flask import request, jsonify
from database.connection import connect_to_database
from database.models import Department, UserDepartmentLink

session = connect_to_database()


def add_department():
    try:
        data = request.json
        department = Department()
        department.name = data['name']
        session.add(department)
        session.commit()
        return jsonify({"Success": f"Department ID{department.id} has beem added"})
    except Exception as e:
        return jsonify({"Error": f"{e}"})
    finally:
        session.close()


def add_user_to_department():
    try:
        data = request.json
        link = UserDepartmentLink()
        link.user_id = data['user_id']
        link.department_id = data['department_id']
        session.add(link)
        session.commit()
        return jsonify({"Success": f"User ID{link.user_id} has been added to department ID{link.department_id}"})
    except Exception as e:
        return jsonify({"Error": f"{e}"})
    finally:
        session.close()


def make_department_dict(record):
    department = {
        'id': record.id,
        'name': record.name
    }
    return department


def convert_department_results(results):
    departments = []
    for record in results:
        department = make_department_dict(record)
        departments.append(department)
    return departments


def get_all_departments():
    try:
        result = session.query(Department).all()
        departments = convert_department_results(result)
        return jsonify(departments)
    except Exception as e:
        return jsonify({"Error": f"{e}"})
    finally:
        session.close()


def get_all_users_in_department(department_id):
    try:
        result = session.query(UserDepartmentLink).filter_by(department_id=department_id).all()
        user_ids = [record.user_id for record in result]
        department_users = {
            'department_id': department_id,
            'user_ids': user_ids
        }
        return department_users
    except Exception as e:
        return jsonify({"Error": f"{e}"})
    finally:
        session.close()


def update_department(department_id):
    try:
        data = request.json
        record = session.query(Department).filter_by(id=department_id).one()
        record.name = data['name']
        session.add(record)
        session.commit()
        return jsonify({"Success": f"Department {department_id} has been renamed"})
    except Exception as e:
        return jsonify({"Error": f"{e}"})
    finally:
        session.close()


def delete_department(department_id):
    try:
        result_department = session.query(Department).filter_by(id=department_id).one()
        session.delete(result_department)
        result_link = session.query(UserDepartmentLink).filter_by(department_id=department_id).all()
        for record in result_link:
            session.delete(record)
        session.commit()
        return jsonify({"Success": f"Department ID{department_id} has been deleted"})
    except Exception as e:
        return jsonify({"Error": f"{e}"})
    finally:
        session.close()


def delete_user_from_department(department_id, user_id):
    try:
        record = session.query(UserDepartmentLink).filter_by(department_id=department_id, user_id=user_id).one()
        session.delete(record)
        session.commit()
        return jsonify({"Success": f"User ID{user_id} has been deleted from department ID{department_id}"})
    except Exception as e:
        return jsonify({"Error": f"{e}"})
    finally:
        session.close()


def delete_all_users_from_department(department_id):
    try:
        result = session.query(UserDepartmentLink).filter_by(department_id=department_id).all()
        for record in result:
            session.delete(record)
        session.commit()
        return jsonify({"Success": f"All users has been deleted from department ID{department_id}"})
    except Exception as e:
        return jsonify({"Error": f"{e}"})
    finally:
        session.close()
