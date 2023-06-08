from validators.user_validator import UserValidator
from flask import Response, Request
from base.request_data import RequestData
from base.base_controller import BaseController
from business_models.users_business_model import UserBusinessModel
from utils.serializer import ResponseSerializer


class UserController(BaseController):
    @classmethod
    def get_by_id(cls, request: Request) -> Response:
        """
                @api {get} /users/{id} Get user by id
                @apiName UsersGetByID
                @apiGroup Users
                @apiDescription Get user by id if exists else 400
                @apiSuccessExample response body example
                {
                  "data": {
                    "id": 2,
                    "model_type": "users",
                    "attributes": {
                      "id": "2",
                      "first_name": "admin",
                      "last_name": "admin",
                      "phone": "88005553535",
                      "created_at": "2023-04-24 17:14:08",
                      "created_by": "1",
                      "updated_at": "2023-04-24 17:14:08",
                      "updated_by": "1",
                      "deleted_at": null,
                      "deleted_by": null
                    }
                  },
                  "included": {}
                }
                """
        return super(UserController, cls).get_by_id(request)

    @classmethod
    def get(cls, request: Request) -> Response:
        """
               @api {get} /users Get users array
               @apiName UsersGet
               @apiGroup Users
               @apiDescription Get all users in array
               @apiSuccessExample response body example
               {
                 "data": [
                   {
                     "id": 1,
                     "model_type": "users",
                     "attributes": {
                       "id": "1",
                       "first_name": "admin",
                       "last_name": "admin",
                       "phone": "88005553535",
                       "created_at": "2023-04-24 17:14:08",
                       "created_by": "1",
                       "updated_at": "2023-04-24 17:14:08",
                       "updated_by": "1",
                       "deleted_at": null,
                       "deleted_by": null
                     }
                   },
                   {
                     "id": 2,
                     "model_type": "users",
                     "attributes": {
                       "id": "2",
                       "first_name": "user",
                       "last_name": "user",
                       "phone": "89116664646",
                       "created_at": "2023-04-24 17:14:08",
                       "created_by": "1",
                       "updated_at": "2023-04-24 17:14:08",
                       "updated_by": "1",
                       "deleted_at": null,
                       "deleted_by": null
                     }
                   }
                 ],
                 "included": {}
               }
               """
        return super(UserController, cls).get(request)

    @classmethod
    def post(cls, request: Request) -> Response:
        """
                @api {post} /users Crate new user
                @apiName UsersCreate
                @apiGroup Users
                @apiDescription Create new users
                @apiExample json request body example
                {
                  "data": {
                    "attributes": {
                      "first_name": "Vasily",
                      "last_name": "Petrov",
                      "phone": "88005553535"
                      "username": "PetrovVasya",
                      "password": "qwerty123"
                    }
                  }
                }
                @apiSuccessExample response body example
                {
                  "data": {
                    "id": 4,
                    "model_type": "users",
                    "attributes": {
                      "id": "4",
                      "first_name": "Vasily",
                      "last_name": "Petrov",
                      "phone": "88005553535",
                      "created_at": "2023-04-24 17:14:08",
                      "created_by": "2",
                      "updated_at": "2023-04-24 17:14:08",
                      "updated_by": null,
                      "deleted_at": null,
                      "deleted_by": null
                    }
                  },
                  "included": {}
                }
                """
        request_data = RequestData.create(request)
        UserValidator.post(request_data)
        bm = UserBusinessModel(request_data)
        entity = bm.create()
        return ResponseSerializer().serialize_object(entity).response

    @classmethod
    def put(cls, request: Request) -> Response:
        """
                @api {put} /users/{id} Update users
                @apiName UsersUpdate
                @apiGroup Users
                @apiDescription Update user by id
                @apiExample json request body example
                {
                  "data": {
                    "attributes": {
                      "first_name": "Petr"
                    }
                  }
                }
                @apiSuccessExample response body example
                {
                  "data": {
                    "id": 4,
                    "model_type": "users",
                    "attributes": {
                      "id": "4",
                      "first_name": "Petr",
                      "last_name": "Petrov",
                      "phone": "88005553535",
                      "created_at": "2023-04-24 17:14:08",
                      "created_by": "2",
                      "updated_at": "2023-04-24 17:34:49",
                      "updated_by": "2",
                      "deleted_at": null,
                      "deleted_by": null
                    }
                  },
                  "included": {}
                }
                """
        request_data = RequestData.create(request)
        UserValidator.put(request_data)
        bm = UserBusinessModel(request_data)
        entity = bm.update()
        return ResponseSerializer().serialize_object(entity).response

    @classmethod
    def delete(cls, request: Request) -> Response:
        """
                @api {delete} /users/{id} Delete user
                @apiName UsersDelete
                @apiGroup Users
                @apiDescription Delete user by id
                @apiSuccessExample response body example
                {
                  "data": {
                    "id": 4,
                    "model_type": "users",
                    "attributes": {
                      "id": "4",
                      "first_name": "Petr",
                      "last_name": "Petrov",
                      "phone": "88005553535",
                      "created_at": "2023-04-24 17:14:08",
                      "created_by": "2",
                      "updated_at": "2023-04-24 17:34:49",
                      "updated_by": "2",
                      "deleted_at": "2023-04-24 17:40:02",
                      "deleted_by": "2"
                    }
                  },
                  "included": {}
                }
                """
        return super(UserController, cls).delete(request)
