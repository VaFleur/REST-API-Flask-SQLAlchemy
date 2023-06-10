from controllers.email_controller import EmailController
from controllers.department_controller import DepartmentController
from controllers.user_controller import UserController
from base.base_controller import BaseController
from flask import Flask

model_controllers = [
    # users
    {"rule": "/users", "endpoint": "user_get", "methods": ["GET"], "view_func": UserController.get},
    {"rule": "/users/<id>", "endpoint": "user_get_by_id", "methods": ["GET"], "view_func": UserController.get_by_id},
    {"rule": "/users", "endpoint": "user_post", "methods": ["POST"], "view_func": UserController.post},
    {"rule": "/users/<id>", "endpoint": "user_put", "methods": ["PUT"], "view_func": UserController.put},
    {"rule": "/users/<id>", "endpoint": "user_delete", "methods": ["DELETE"], "view_func": UserController.delete},

    # departments
    {"rule": "/departments", "endpoint": "department_get", "methods": ["GET"], "view_func": DepartmentController.get},
    {"rule": "/departments/<id>", "endpoint": "department_get_by_id", "methods": ["GET"], "view_func": DepartmentController.get_by_id},
    {"rule": "/departments", "endpoint": "department_post", "methods": ["POST"], "view_func": DepartmentController.post},
    {"rule": "/departments/<id>", "endpoint": "department_put", "methods": ["PUT"], "view_func": DepartmentController.put},
    {"rule": "/departments/<id>", "endpoint": "department_delete", "methods": ["DELETE"], "view_func": DepartmentController.delete},

    # emails
    {"rule": "/emails", "endpoint": "email_get", "methods": ["GET"], "view_func": EmailController.get},
    {"rule": "/emails/<id>", "endpoint": "email_get_by_id", "methods": ["GET"], "view_func": EmailController.get_by_id},
    {"rule": "/emails", "endpoint": "email_post", "methods": ["POST"], "view_func": EmailController.post},
    {"rule": "/emails/<id>", "endpoint": "email_put", "methods": ["PUT"], "view_func": EmailController.put},
    {"rule": "/emails/<id>", "endpoint": "email_delete", "methods": ["DELETE"], "view_func": EmailController.delete},
]


def register_routes(app: Flask):
    for model_controller in model_controllers:
        app.add_url_rule(
            rule=model_controller["rule"],
            endpoint=model_controller["endpoint"],
            methods=model_controller["methods"],
            view_func=model_controller["view_func"]
        )

    app.add_url_rule(rule="/<entity_type>", endpoint="base_get", methods=["GET"], view_func=BaseController.get)
    app.add_url_rule(rule="/<entity_type>/<id>", endpoint="base_get_by_id", methods=["GET"], view_func=BaseController.get_by_id)
    app.add_url_rule(rule="/<entity_type>", endpoint="base_post",  methods=["POST"], view_func=BaseController.post)
    app.add_url_rule(rule="/<entity_type>/<id>", endpoint="base_put", methods=["PUT"], view_func=BaseController.put)
    app.add_url_rule(rule="/<entity_type>/<id>", endpoint="base_delete", methods=["DELETE"], view_func=BaseController.delete)
