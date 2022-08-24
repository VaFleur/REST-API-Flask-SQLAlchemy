from flask import request, jsonify
from database.connection import connect_to_database
from database.models import Email

session = connect_to_database()


def add_email():
    try:
        data = request.json
        email = Email()
        email.adress = data['adress']
        email.user_id = data['user_id']
        session.add(email)
        session.commit()
        return jsonify({"Success": f"Email for user ID{email.user_id} has been added"})
    except Exception as e:
        return jsonify({"Error": f"{e}"})
    finally:
        session.close()


def delete_all_emails(user_id):
    try:
        result = session.query(Email).filter_by(user_id=user_id).all()
        for record in result:
            session.delete(record)
        session.commit()
        return jsonify({"Success": f"All email adresses for user ID{user_id} has been deleted"})
    except Exception as e:
        return jsonify({"Error": f"{e}"})
    finally:
        session.close()


def delete_email(email_id):
    try:
        record = session.query(Email).filter_by(id=email_id).one()
        session.delete(record)
        session.commit()
        return jsonify({"Success": f"Email ID{email_id} has been deleted"})
    except Exception as e:
        return jsonify({"Error": f"{e}"})
    finally:
        session.close()


def make_email_dict(record):
    email = {
        'id': record.id,
        'adress': record.adress,
        'user_id': record.user_id
    }
    return email


def convert_email_results(results):
    emails = []
    for record in results:
        email = make_email_dict(record)
        emails.append(email)
    return emails


def get_all_emails():
    try:
        result = session.query(Email).all()
        emails = convert_email_results(result)
        return jsonify(emails)
    except Exception as e:
        return jsonify({"Error": f"{e}"})
    finally:
        session.close()


def get_emails_for_user(user_id):
    try:
        result = session.query(Email).filter_by(user_id=user_id).all()
        adresses = [record.adress for record in result]
        ids = [record.id for record in result]
        emails = dict(zip(ids, adresses))
        user_emails = {
            'user_id': user_id,
            'user_emails': emails
        }
        return user_emails
    except Exception as e:
        return jsonify({"Error": f"{e}"})
    finally:
        session.close()


def update_email(email_id):
    try:
        data = request.json
        record = session.query(Email).filter_by(id=email_id).one()
        record.adress = data['adress']
        session.add(record)
        session.commit()
        return jsonify({"Success": f"Email ID{email_id} has been updated"})
    except Exception as e:
        return jsonify({"Error": f"{e}"})
    finally:
        session.close()
