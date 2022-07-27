from flask import request, jsonify
from app.application import app
from app.database.models import User, Phone
from app.database.session import session


@app.route('/phone/<int:id>', methods=['POST'])
def add_phone(id):
    pass

@app.route('/phone/', methods=['GET'])
def get_phones():
    pass

@app.route('/phone/<int:id>', methods=['GET'])
def get_phone(id):
    pass

@app.route('/phone/<int:id>', methods=['PUT'])
def update_phone(id):
    pass

@app.route('/phone/<int:id>', methods=['DELETE'])
def delete_phone(id):
    pass