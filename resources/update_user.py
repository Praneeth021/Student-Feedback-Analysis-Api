from flask import jsonify, make_response
from flask_restful import Resource, reqparse, request
from models.user_model import UserModel
from db import db
from flask_jwt_extended import jwt_required, get_jwt_identity

#Resource which helps to update users details

class UpdateUser(Resource):

    @jwt_required
    def put(self):

        current_user= get_jwt_identity()
        user = UserModel.find_by_id(id=current_user)

        user.username=request.json.get('username', user.username)
        user.department=request.json.get('department', user.department)
        user.year=request.json.get('year', user.year)
        user.section=request.json.get('section', user.section)
        user.pasword=request.json.get('password', user.password)
        
        db.session.commit()
        return {"message":"Updated"}, 201

       
        



