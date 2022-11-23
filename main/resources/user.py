from flask_restful import Resource, reqparse
from models.user_model import UserModel
from flask_jwt_extended import create_access_token

params = reqparse.RequestParser()
params.add_argument('first_name', type=str, required=True, help='First name cannot be blank')
params.add_argument('last_name', type=str, required=True, help='Last name cannot be blank')
params.add_argument('u_login', type=str, required=True, help='Login cannot be blank')
params.add_argument('u_password', type=str, required=True, help='Password cannot be blank')


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
            

class UserRegister(Resource):
    
    # /register
    def post(self):
        data = params.parse_args()
        if UserModel.login_exists(data['u_login']):
            return {'message': 'User \'{}\' already exists'.format(data['u_login'])}, 400
        user = UserModel(**data) 
        user.save_user()
        return {'message': 'User created successfully.'}, 201
    

class UserLogin(Resource):

    # /login
    @classmethod
    def post(cls):
        data = params.parse_args()
        user = UserModel.login_exists(data['u_login'])
        # TODO: Make safe comparison for pw
        if user and user.u_password == data['u_password']:
            user_token = create_access_token(identity=user.user_id)
    

            





