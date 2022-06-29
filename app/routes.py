from flask import request, jsonify, Flask
from sqlalchemy import text
from werkzeug.security import generate_password_hash
from sqlalchemy.orm import sessionmaker
from user import Users, engine

app = Flask(__name__)
Session = sessionmaker(bind=engine)
session = Session()

@app.route('/user/', methods=['POST'])
def add_user():
    try:
        new_user = Users(
            username=request.json['username'],
            password=generate_password_hash(request.json['password']),
            email=request.json['email'],
            first_name=request.json['first_name'],
            last_name=request.json['last_name']
        )
        session.add(new_user)
        session.commit()
        return jsonify({"Success": "User id has been added"})
    except:
        return jsonify({"Error": "User id has not been added"})

@app.route('/user/', methods=['GET'])
def get_users():
    res = engine.execute(text("SELECT * FROM users ORDER BY id ASC"))
    lines = [dict(line) for line in res.fetchall()]
    return jsonify(lines)

@app.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    res = engine.execute(text(f"SELECT * FROM users WHERE id = {id} ORDER BY id ASC"))
    lines = [dict(line) for line in res.fetchall()]
    return jsonify(lines)

@app.route('/user/<int:id>', methods=['PUT'])
def update_user(id):
    try:
        u = session.query(Users).get(id)
        u.username = request.json['username']
        u.password = generate_password_hash(request.json['password'])
        u.email = request.json['email']
        u.first_name = request.json['first_name']
        u.last_name = request.json['last_name']

        session.add(u)
        session.commit()
        return jsonify({"Success": f"User id{id} has been updated"})
    except:
        return jsonify({"Error": f"User id{id} has not been updated"})

@app.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    try:
        u = session.query(Users).get(id)
        session.delete(u)
        session.commit()
        return jsonify({"Success": f"User id{id} has been deleted"})
    except:
        return jsonify({"Error": f"User id{id} has not been deleted"})