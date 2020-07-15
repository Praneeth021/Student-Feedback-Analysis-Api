from flask import jsonify, make_response
from flask_restful import Resource, reqparse, request
from models.teachers_model import TeacherModel
from models.user_model import UserModel
from db import db
from flask_jwt_extended import jwt_required, get_jwt_identity

class UpdateTeacher(Resource):
    
    @jwt_required
    def put(self):

        current_user = get_jwt_identity()
        user = UserModel.query.filter_by(id=current_user).first()
        user = user.to_dict()

        tid=request.json.get('tid')
        teacher=TeacherModel.find_by_tid(tid=tid)

        if not (user['admin']):
            return make_response(jsonify({"msg": "You are not authorised to access the page"}), 403)
        if  TeacherModel.find_by_tid(tid=tid):
            teacher.username=request.json.get('username', teacher.username)
            teacher.department=request.json.get('department', teacher.department)
            teacher.gender=request.json.get('gender', teacher.gender)
            teacher.image=request.json.get('image', teacher.image)
            teacher.designation=request.json.get('designation', teacher.designation)
            teacher.email= request.json.get('email',teacher.email)
            teacher.date_joined=request.json.get('date_joined', teacher.date_joined)
                
            db.session.commit()
            return {"message":"Updated"}, 201

        return make_response(jsonify({"message":"Not Exists"}), 401)
        



