import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username", required=True, type=str)
    parser.add_argument("password", required=True, type=str)

    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data["username"]):
            return {"msg": "'{}' already exists.".format(data["username"])}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {
            "msg": "The User '{}' was created successfully.".format(data["username"])
        }, 201
