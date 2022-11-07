from flask_restful import Resource, reqparse
from models.user_model import UserModel

# /users/<int:user_id>
class User(Resource):
    def get(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            return user.parse_to_json(), 200
        else:
            return {'message': 'User not found'}, 404

    def delete(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            user.delete_user()
            return {'message': 'User deleted'}, 200
        else:
            return {'message': 'User not found'}, 404
            

class AuthService(Resource):
    
    def post(self):
        params = reqparse.RequestParser()
        params.add_argument('first_name', type=str, required=True, help='First name cannot be blank')
        params.add_argument('last_name', type=str, required=True, help='Last name cannot be blank')
        params.add_argument('u_login', type=str, required=True, help='Login cannot be blank')
        params.add_argument('u_password', type=str, required=True, help='Password cannot be blank')

        data = AuthService.params.parse_args()
        if UserModel.find_user(data['u_login']):
            return {'message': 'User already exists'}, 400
        user = UserModel(**data)
        user.save_user()
        return user.parse_to_json(), 201
    

