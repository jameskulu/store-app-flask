from flask_restful import Resource, reqparse
from flask import jsonify
from flask_jwt_extended import create_access_token, jwt_required
from flask_jwt_extended import current_user
from app.models.user import UserModel
from app.util.encoder import AlchemyEncoder
import json
from app.util.logz import create_logger


class Login(Resource):
    def __init__(self):
        self.logger = create_logger()

    parser = reqparse.RequestParser()  # only allow price changes, no name changes allowed
    parser.add_argument('username', type=str, required=True,
                        help='This field cannot be left blank')
    parser.add_argument('password', type=str, required=True,
                        help='This field cannot be left blank')

    def post(self):
        data = Login.parser.parse_args()
        username = data['username']
        password = data['password']

        user = UserModel.query.filter_by(username=username).one_or_none()
        if not user or not user.check_password(password):
            return {'message': 'Invalid Credentials.'}, 401
        access_token = create_access_token(
            identity=json.dumps(user, cls=AlchemyEncoder))
        return jsonify(access_token=access_token)

    @jwt_required() 
    def get(self):
        return jsonify(
            id=current_user.id,
            full_name=current_user.full_name,
            username=current_user.username,
        )


class Register(Resource):
    def __init__(self):
        self.logger = create_logger()

    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True,
                        help='This field cannot be left blank')
    parser.add_argument('password', type=str, required=True,
                        help='This field cannot be left blank')

    def post(self):
        data = Register.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message': 'User already exists'}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {'message': 'User has been created successfully.'}, 201
