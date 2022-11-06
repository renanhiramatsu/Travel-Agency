from flask_restful import Resource, reqparse
from models.user_model import UserModel

class Users(Resource):
    def get(self):
        return {'users': [user.parse_to_json() for hotel in UserModel.query.all()]}

class User(Resource):
    params = reqparse.RequestParser()
    params.add_argument('first_name', type=str, required=True, help='First name cannot be blank')
    params.add_argument('last_name', type=str, required=True, help='Last name cannot be blank')

    def get(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            return user.parse_to_json(), 200
        else:
            return {'message': 'User not found'}, 404


