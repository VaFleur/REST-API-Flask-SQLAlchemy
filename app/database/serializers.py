

def serialize_user(result):
    users = []
    for record in result:
        user = {
            'id': record.id,
            'username': record.username,
            'password': record.password,
            'first_name': record.first_name,
            'last_name': record.last_name,
            'phone': record.phone
        }
        users.append(user)
    return users


def serialize_email(result):
    emails = []
    for record in result:
        email = {
            'id': record.id,
            'adress': record.adress,
            'user_id': record.user_id
        }
        emails.append(email)
    return emails


def serialize_department(result):
    departments = []
    for record in result:
        department = {
            'id': record.id,
            'name': record.name
        }
        departments.append(department)
    return departments
