from flask import jsonify
from flask_restful import Resource, reqparse
from models.class_model import ClassModel

class EnterClass(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('department', type=str, required=True)
    parser.add_argument('year', type=str, required=True)
    parser.add_argument('section', type=str, required=True)
    parser.add_argument('subject', type= str, required=True)
    parser.add_argument('teacher_id', type=str)

    def post(self):

        data=EnterClass.parser.parse_args()

        if ClassModel.find_by_department(data['department'], data['year'], data['section'], data['subject']):
            return {"message":"Already Exists"}, 400

        user= ClassModel(department= data['department'], year= data['year'], section= data['section'],
                                         subject=data['subject'], teacher_id= data['teacher_id'])
        user.save_to_db()

        return {"message": "Added Successfully"}, 201