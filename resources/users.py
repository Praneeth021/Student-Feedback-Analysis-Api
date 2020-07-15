from flask import make_response,jsonify
from flask_restful import Resource
from models.user_model import UserModel
from sqlalchemy_serializer import SerializerMixin
from flask_jwt_extended import jwt_required,get_jwt_identity



#Resource to get all the student users
class Users(Resource):

    @jwt_required
    def get(self):
        current_user=get_jwt_identity()
        user=UserModel.query.filter_by(id=current_user).first()
        user=user.to_dict()
        if not (user['admin']) :
            return make_response(jsonify({"message":"Your are not authorised to access this resource"}),403)
        data=UserModel.query.all()
        result=[]
        for i in data:
            i=i.to_dict()
            if(i['admin']==False):
                result.append(i)
        return make_response(jsonify(result),201)

    

#Resource for getting the user currently logged in
class CurrentUser(Resource):

    @jwt_required
    def get(self):
        
        current_user=get_jwt_identity()
        user=UserModel.query.filter_by(id=current_user).first()
        if user:
            user=user.to_dict()
            return make_response(jsonify(user),201)
        
        return make_response(jsonify({"msg":"Requested Object not found"},403))
            


