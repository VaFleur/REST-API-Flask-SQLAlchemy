from database.connection import connect_to_database
from database.models import Department, UserDepartmentLink

session = connect_to_database()


def add_department(data):
    try:
        department = Department()
        department.name = data['name']
        session.add(department)
        session.commit()
        print(f'Department ID{department.id} has beem added')
    except Exception as e:
        print(e)
    finally:
        session.close()


def add_user_to_department(data):
    try:
        link = UserDepartmentLink()
        link.user_id = data['user_id']
        link.department_id = data['department_id']
        session.add(link)
        session.commit()
        print(f'User ID{link.user_id} has been added to department ID{link.department_id}')
    except Exception as e:
        print(e)
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
        return departments
    except Exception as e:
        print(e)
    finally:
        session.close()


def get_all_users_in_department(department_id):
    try:
        result = session.query(UserDepartmentLink).filter_by(departmnet_id=department_id).all()
        user_ids = [record.user_id for record in result]
        department_users = {
            'department_id': department_id,
            'user_ids': user_ids
        }
        return department_users
    except Exception as e:
        print(e)
    finally:
        session.close()


def update_department(department_id, data):
    try:
        record = session.query(UserDepartmentLink).filter_by(departmnet_id=department_id).one()
        record.name = data['name']
        session.add(record)
        session.commit()
        print(f'Department {department_id} has been renamed')
    except Exception as e:
        print(e)
    finally:
        session.close()


def delete_department(department_id):
    try:
        record_department = session.query(Department).filter_by(id=department_id).one()
        record_link = session.query(UserDepartmentLink).filter_by(department_id=department_id).all()
        session.delete(record_department)
        session.delete(record_link)
        session.commit()
        print(f'Department ID{department_id} has been deleted')
    except Exception as e:
        print(e)
    finally:
        session.close()


def delete_user_from_department(data):
    try:
        user_id = data['user_id']
        department_id = data['department_id']
        record = session.query(UserDepartmentLink).filter_by(department_id=department_id, user_id=user_id).one()
        session.delete(record)
        session.commit()
        print(f'User ID{user_id} has been deleted from department ID{department_id}')
    except Exception as e:
        print(e)
    finally:
        session.close()


def delete_all_users_from_department(department_id):
    try:
        record = session.query(UserDepartmentLink).filter_by(department_id=department_id).all()
        session.delete(record)
        session.commit()
        print(f'All users has been deleted from department ID{department_id}')
    except Exception as e:
        print(e)
    finally:
        session.close()
