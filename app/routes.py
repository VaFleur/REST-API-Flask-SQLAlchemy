from controllers.article_controller import ArticleController
from controllers.comment_controller import CommentController
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

    # comments
    {"rule": "/comments", "endpoint": "comment_get", "methods": ["GET"], "view_func": CommentController.get},
    {"rule": "/comments/<id>", "endpoint": "comment_get_by_id", "methods": ["GET"], "view_func": CommentController.get_by_id},
    {"rule": "/comments", "endpoint": "comment_post", "methods": ["POST"], "view_func": CommentController.post},
    {"rule": "/comments/<id>", "endpoint": "comment_put", "methods": ["PUT"], "view_func": CommentController.put},
    {"rule": "/comments/<id>", "endpoint": "comment_delete", "methods": ["DELETE"], "view_func": CommentController.delete},

    # articles
    {"rule": "/articles", "endpoint": "article_get", "methods": ["GET"], "view_func": ArticleController.get},
    {"rule": "/articles/<id>", "endpoint": "article_get_by_id", "methods": ["GET"], "view_func": ArticleController.get_by_id},
    {"rule": "/articles", "endpoint": "article_post", "methods": ["POST"], "view_func": ArticleController.post},
    {"rule": "/articles/<id>", "endpoint": "article_put", "methods": ["PUT"], "view_func": ArticleController.put},
    {"rule": "/articles/<id>", "endpoint": "article_delete", "methods": ["DELETE"], "view_func": ArticleController.delete},
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
