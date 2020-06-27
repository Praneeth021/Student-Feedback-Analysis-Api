from flask import jsonify
from flask_restful import Resource, reqparse
from models.class_model import ClassModel

class Classes(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('department', type=str, required=True)
    parser.add_argument('year', type=str, required=True)
    parser.add_argument('section', type=str, required=True)
    parser.add_argument('subject', type= str, required=True)
    parser.add_argument('teacher_id', type=str)

    def post(self):

        data=Classes.parser.parse_args()

        if ClassModel.find_by_department(data['department'], data['year'], data['section'], data['subject']):
            return {"message":"Already Exists"}, 400

        className= ClassModel()
        className.department= data['department']
        className.year= data['year'] 
        className.usersection= data['section']
        className.subject=data['subject']
        className.teacher_id= data['teacher_id']
        className.save_to_db()

        return {"message": "Added Successfully"}, 201