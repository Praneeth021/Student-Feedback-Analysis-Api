from flask import jsonify
from flask_restful import Resource, reqparse
from models.user_model import UserModel


class Register(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('rollno',type=str,required=True,help="this field cannot be blank")
    parser.add_argument('username',type=str,required=True,help="This field cannot be blank")
    parser.add_argument('password',type=str,required=True,help="This field cannot be blank")


    def post(self):
        data=Register.parser.parse_args()

        print(data['username'])

        if UserModel.find_by_id(data['rollno']):
            return {"message":"You are already registered"},400
        
        user=UserModel(rollno=data['rollno'],username=data['username'],password=data['password'])
        user.save_to_db()

        return {'message':"Your account created successfully"},201