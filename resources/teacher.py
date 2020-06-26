from flask import jsonify
from flask_restful import Resource, reqparse
from models.techers_model import TeacherModel


class Teacher(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('tid',type=str,required=True,help="this field cannot be blank")
    parser.add_argument('username',type=str,required=True)
    parser.add_argument('dept',type=str,required=True)
    parser.add_argument('gender',type=str,required=True)
    parser.add_argument('image',type=str)
    parser.add_argument('desig',type=str,required=True)
    parser.add_argument('email',type=str,required=True)
    parser.add_argument('date_join',type=str,required=True)


    def post(self):
        data=Teacher.parser.parse_args()
        
        if TeacherModel.find_by_tid(data['tid']):
            return {"message":"Already exists"},400


        u=TeacherModel(tid=data['tid'],username=data['username'],dept=data['dept'],
                        gender=data['gender'],image=data['image'],desig=data['desig'],
                         email=data['email'], date_join=data['date_join'])

        u.save_to_db()
        return {"message":"successfully added"},201