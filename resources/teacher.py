from flask import jsonify
from flask_restful import Resource, reqparse
from models.teachers_model import TeacherModel
from flask_jwt_extended import jwt_required


class Teacher(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('tid',type=str,required=True,help="this field cannot be blank")
    parser.add_argument('username',type=str,required=True,help="Username cannot be blank")
    parser.add_argument('department',type=str,required=True,help="Department cannnot be blank")
    parser.add_argument('gender',type=str,required=True,help="Gender cannot be blank")
    parser.add_argument('image',type=str)
    parser.add_argument('designation',type=str,required=True,help="Designation cannot be blank")
    parser.add_argument('email',type=str,required=True,help="Email cannot be blank")
    parser.add_argument('date_joined',type=str,required=True,help="Date Joined cannot be blank")

    @jwt_required
    def post(self):
        data=Teacher.parser.parse_args()
        
        if TeacherModel.find_by_tid(data['tid']):
            return {"message":"Already exists"},400


        teacher=TeacherModel(tid=data['tid'],username=data['username'],designation=data['designation'],deptartment=data['department'],gender=data['gender'],date_joined=data['date_joined'],image=data['image'],email=data['email'])
        teacher.save_to_db()
        return {"message":"successfully added"},201
