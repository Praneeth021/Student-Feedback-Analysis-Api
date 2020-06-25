from flask import jsonify,make_response
from flask_jwt_extended import create_access_token,jwt_required
from flask_restful import Resource,reqparse
from models.user_model import UserModel


class Login(Resource):
    
    parser=reqparse.RequestParser()
    parser.add_argument('rollno',type=str,required=True,help="this field cannot be blank")
    parser.add_argument('password',type=str,required=True,help="This field cannot be blank")
    

    def post(self):
        data=Login.parser.parse_args()
        
        rollno = data['rollno']
        password = data['password']
        if not rollno:
            return make_response(jsonify({"msg": "Missing username parameter"}), 400)
        if not password:
            return make_response(jsonify({"msg": "Missing password parameter"}), 400)

        if(UserModel.find_by_id(rollno)):
            access_token = create_access_token(identity=rollno)
            return make_response(jsonify(access_token=access_token), 200)
        
        return make_response(jsonify({"msg":"Incorrect Credentials"}),400)
        


