from flask import request, jsonify
from bussines_logic.user_bussines_logic import add_user, delete_user, update_user, get_all_users, get_user


def add_user_controller():
    try:
        user_data = request.json
        user = add_user(user_data)

        if user is not None:
            return jsonify({"Success": f"User id{user.id} has been added"})
        else:
            return jsonify({"Error": "Cannot create user"})

    except Exception as e:
        return jsonify({"Error": f"{e}"})


def delete_user_controller(user_id: int):
    try:
        delete_user(user_id)
        return jsonify({"Success": f"User id{user_id} has been deleted"})

    except Exception as e:
        return jsonify({"Error": f"{e}"})


def update_user_controller(user_id):
    try:
        user_data = request.json
        user = update_user(user_data, user_id)

        if user is not None:
            return jsonify({"Success": f"User id{user_id} has been updated"})
        else:
            return jsonify({"Error": "Cannot update user"})

    except Exception as e:
        return jsonify({"Error": f"{e}"})


def get_all_users_controller():
    try:
        users = get_all_users()

        if users is not None:
            return jsonify(users)
        else:
            return jsonify({"Error": "Cannot get user data"})

    except Exception as e:
        return jsonify({"Error": f"{e}"})


def get_user_controller(user_id):
    try:
        user = get_user(user_id)

        if user is not None:
            return jsonify(user)
        else:
            return jsonify({"Error": "Cannot get user data"})

    except Exception as e:
        return jsonify({"Error": f"{e}"})
