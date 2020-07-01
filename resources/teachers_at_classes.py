from flask import make_response,jsonify
from flask_restful import Resource, reqparse
from models.class_model import ClassModel
from models.teachers_model import TeacherModel
from sqlalchemy_serializer import SerializerMixin
from flask_jwt_extended import jwt_required,get_jwt_identity



#Resouce which gives information about the teachers going to a particular class

class FindClass(Resource):

    parser=reqparse.RequestParser()
    parser.add_argument('department', type=str, required=True)
    parser.add_argument('year', type=str, required=True)
    parser.add_argument('section', type=str, required=True)

    @jwt_required
    def get(self):

        data=FindClass.parser.parse_args()

        result= ClassModel.find_by_class(data['department'], data['year'], data['section'])
        d=list()
        for i in result:
            x=i.to_dict()
            d.append(TeacherModel.find_by_tid(x['teacher_id']).to_dict())
        return make_response(jsonify(d),201)
        

