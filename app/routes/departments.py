from flask import request, jsonify
from app.application import app
from app.database.models import User, Department
from app.database.session import session


@app.route('/department/<int:id>', methods=['POST'])
def add_department(id):
    pass

@app.route('/department/', methods=['GET'])
def get_departments():
    pass

@app.route('/department/<int:id>', methods=['GET'])
def get_department(id):
    pass

@app.route('/department/<int:id>', methods=['PUT'])
def update_department(id):
    pass

@app.route('/department/<int:id>', methods=['DELETE'])
def delete_department(id):
    pass