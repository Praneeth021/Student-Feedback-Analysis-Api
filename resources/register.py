from flask import jsonify,make_response
from flask_restful import Resource, reqparse
from models.user_model import UserModel


#Resource for registering the user 
class Register(Resource):

    parser=reqparse.RequestParser()
    parser.add_argument('rollno',type=str,required=True,help="this field cannot be blank")
    parser.add_argument('username',type=str,required=True,help="This field cannot be blank")
    parser.add_argument('password',type=str,required=True,help="This field cannot be blank")
    parser.add_argument('department',type=str,required=True,help="This field cannot be blank")
    parser.add_argument('section',type=str,required=True,help="This field cannot be blank")
    parser.add_argument('year',type=str,required=True,help='This field cannot be blank')
    parser.add_argument('admin',type=bool)



    def post(self):


        data=Register.parser.parse_args()

        if UserModel.find_by_id(data['rollno']):
            return {"message":"You are already registered"},400

        if data['admin']:
            if UserModel.query.filter_by(admin=True):
                return make_response(jsonify({"msg":"Admin already exists"}),403)
            user=UserModel(rollno=data['rollno'],username=data['username'],password=data['password'],department=data['department'],year=data['year'],section=data['section'],admin=True)
        
        user=UserModel(rollno=data['rollno'],username=data['username'],password=data['password'],department=data['department'],year=data['year'],section=data['section'])
        user.save_to_db()

        return {'message':"Your account created successfully"},201