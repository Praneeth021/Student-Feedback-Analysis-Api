from flask import make_response,jsonify
from flask_restful import Resource
from models.user_model import UserModel
from sqlalchemy_serializer import SerializerMixin

class U(Resource):

    def get(self):
        data=UserModel.query.all()
        result=[]
        for i in data:
            result.append(i.to_dict())

        return make_response(jsonify(result),201)
            


