from flask import make_response,jsonify
from flask_restful import Resource
from models.user_model import UserModel
from sqlalchemy_serializer import SerializerMixin
from flask_jwt_extended import jwt_required

class Users(Resource):

    @jwt_required
    def get(self):
        data=UserModel.query.all()
        result=[]
        for i in data:
            result.append(i.to_dict())

        return make_response(jsonify(result),201)

    
class UsersByRollno(Resource):

    @jwt_required
    def get(self,rollno):
        if UserModel.find_by_id(rollno):
            data=UserModel.query.filter_by(rollno=rollno).first()
            result=data.to_dict()
            return make_response(jsonify(result),201)
        
        return make_response(jsonify({"msg":"Requested Object not found"},403))
            


