from controllers import EmailController, DepartmentController, UserController
from base import BaseController
from application import app

model_controllers = [
    # users
    {"rule": "/users", "methods": ["GET"], "view_func": UserController.get},
    {"rule": "/users/<id>", "methods": ["GET"], "view_func": UserController.get_by_id},
    {"rule": "/users", "methods": ["POST"], "view_func": UserController.post},
    {"rule": "/users/<id>", "methods": ["PUT"], "view_func": UserController.put},
    {"rule": "/users/<id>", "methods": ["DELETE"], "view_func": UserController.delete},

    # departments
    {"rule": "/departments", "methods": ["GET"], "view_func": DepartmentController.get},
    {"rule": "/departments/<id>", "methods": ["GET"], "view_func": DepartmentController.get_by_id},
    {"rule": "/departments", "methods": ["POST"], "view_func": DepartmentController.post},
    {"rule": "/departments/<id>", "methods": ["PUT"], "view_func": DepartmentController.put},
    {"rule": "/departments/<id>", "methods": ["DELETE"], "view_func": DepartmentController.delete},

    # emails
    {"rule": "/emails", "methods": ["GET"], "view_func": EmailController.get},
    {"rule": "/emails/<id>", "methods": ["GET"], "view_func": EmailController.get_by_id},
    {"rule": "/emails", "methods": ["POST"], "view_func": EmailController.post},
    {"rule": "/emails/<id>", "methods": ["PUT"], "view_func": EmailController.put},
    {"rule": "/emails/<id>", "methods": ["DELETE"], "view_func": EmailController.delete},
]


def register_routes(app_: app):
    for model_controller in model_controllers:
        app_.add_url_rule(
            rule=model_controller["rule"],
            methods=model_controller["methods"],
            view_func=model_controller["view_func"]
        )

    app_.add_url_rule(rule="/<entity_type>", methods=["GET"], view_func=BaseController.get)
    app_.add_url_rule(rule="/<entity_type>/<id>", methods=["GET"], view_func=BaseController.get_by_id)
    app_.add_url_rule(rule="/<entity_type>", methods=["POST"], view_func=BaseController.post)
    app_.add_url_rule(rule="/<entity_type>/<id>", methods=["PUT"], view_func=BaseController.put)
    app_.add_url_rule(rule="/<entity_type>/<id>", methods=["DELETE"], view_func=BaseController.delete)