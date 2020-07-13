from flask import make_response, jsonify
from flask_restful import Resource, reqparse
from models.class_model import ClassModel
from models.user_model import UserModel
from models.teachers_model import TeacherModel
from sqlalchemy_serializer import SerializerMixin
from flask_jwt_extended import jwt_required, get_jwt_identity


# Resouce which gives information about the teachers going to a particular class

class FindClass(Resource):

    @jwt_required
    def get(self):

        current_user = get_jwt_identity()
        user = UserModel.find_by_id(id=current_user).to_dict()
        result = ClassModel.find_by_class(
            user['department'], user['year'], user['section'])
        d = list()
        for i in result:
            x = i.to_dict()
            d.append(TeacherModel.find_by_tid(x['teacher_id']).to_dict())
        return make_response(jsonify(d), 201)

