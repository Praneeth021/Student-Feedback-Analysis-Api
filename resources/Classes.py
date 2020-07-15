from flask import jsonify,make_response
from flask_restful import Resource, reqparse
from models.class_model import ClassModel
from models.user_model import UserModel
from flask_jwt_extended import jwt_required,get_jwt_identity

#Resource for adding teachers to particular class section and year
class Classes(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('department', type=str, required=True)
    parser.add_argument('year', type=str, required=True)
    parser.add_argument('section', type=str, required=True)
    parser.add_argument('subject', type=str, required=True)
    parser.add_argument('teacher_id', type=str)

    @jwt_required
    def post(self):

        data = Classes.parser.parse_args()

        current_user = get_jwt_identity()
        user = UserModel.query.filter_by(id=current_user).first().to_dict()
        if not user['admin']:
            return make_response(jsonify({'msg":Your are not authorised'}),403)
        
        if ClassModel.find_by_department(data['department'], data['year'], data['section'], data['subject']):
            return {"message": "Already Exists"}, 400

        className = ClassModel()
        className.department = data['department']
        className.year = data['year']
        className.usersection = data['section']
        className.subject = data['subject']
        className.teacher_id = data['teacher_id']
        className.save_to_db()

        return {"message": "Added Successfully"}, 201
