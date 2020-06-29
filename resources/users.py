from flask import make_response,jsonify
from flask_restful import Resource
from models.user_model import UserModel
from sqlalchemy_serializer import SerializerMixin

class Users(Resource):

    def get(self):
        data=UserModel.query.all()
        result=[]
        for i in data:
            result.append(i.to_dict())

        return make_response(jsonify(result),201)

    
class UsersByRollno(Resource):

    def get(self,rollno):
        if UserModel.find_by_id(rollno):
            data=UserModel.query.filter_by(rollno=rollno).first()
            result=data.to_dict()
            return make_response(jsonify(result),201)
        
        return make_response(jsonify({"msg":"Requested Object not found"},403))
            


