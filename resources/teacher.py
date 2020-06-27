from flask import jsonify
from flask_restful import Resource, reqparse
from models.teachers_model import TeacherModel


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


    def post(self):
        data=Teacher.parser.parse_args()
        
        if TeacherModel.find_by_tid(data['tid']):
            return {"message":"Already exists"},400


        teacher=TeacherModel()
        teacher.tid=data['tid']
        teacher.username=data['username']
        teacher.designation=data['designation']
        teacher.department=data['department']
        teacher.gender=data['gender']
        teacher.data_joined=data['date_joined']
        teacher.email=data['email']

        teacher.save_to_db()
        return {"message":"successfully added"},201
