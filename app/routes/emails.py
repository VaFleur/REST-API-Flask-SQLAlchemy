from flask import request, jsonify
from app.application import app
from app.database.models import User, Email
from app.database.session import session


@app.route('/email/<int:id>', methods=['POST'])
def add_email(id):
    pass

@app.route('/email/', methods=['GET'])
def get_emails():
    pass

@app.route('/email/<int:id>', methods=['GET'])
def get_email(id):
    pass

@app.route('/email/<int:id>', methods=['PUT'])
def update_email(id):
    pass

@app.route('/email/<int:id>', methods=['DELETE'])
def delete_email(id):
    pass