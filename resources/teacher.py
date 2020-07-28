from flask import jsonify, make_response
from flask_restful import Resource, reqparse
from models.teachers_model import TeacherModel
from models.user_model import UserModel
from flask_jwt_extended import jwt_required, get_jwt_identity


# Resource for adding Teachers


class Teacher(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('tid', type=str, required=True,
                        help="this field cannot be blank")
    parser.add_argument('username', type=str, required=True,
                        help="Username cannot be blank")
    parser.add_argument('department', type=str, required=True,
                        help="Department cannnot be blank")
    parser.add_argument('gender', type=str, required=True,
                        help="Gender cannot be blank")
    parser.add_argument('image', type=str)
    parser.add_argument('designation', type=str, required=True,
                        help="Designation cannot be blank")
    parser.add_argument('email', type=str, required=True,
                        help="Email cannot be blank")
    parser.add_argument('date_joined', type=str, required=True,
                        help="Date Joined cannot be blank")

    @jwt_required
    def post(self):
        data = Teacher.parser.parse_args()
        current_user = get_jwt_identity()
        user = UserModel.query.filter_by(rollno=current_user).first()
        user = user.to_dict()
        if not (user['admin']):
            return make_response(jsonify({"msg": "You are not authorised to access the page"}), 403)

        if TeacherModel.find_by_tid(data['tid']):
            return {"message": "Already exists"}, 400

        teacher = TeacherModel(tid=data['tid'], username=data['username'], designation=data['designation'], department=data['department'],
                               gender=data['gender'], date_joined=data['date_joined'], image=data['image'], email=data['email'])
        teacher.save_to_db()
        return {"message": "successfully added"}, 201


# Resouce for getting information of all Teachers

class AllTeachers(Resource):

    @jwt_required
    def get(self):

        current_user = get_jwt_identity()
        user = UserModel.query.filter_by(rollno=current_user).first()
        user = user.to_dict()
        if not (user['admin']):
            return make_response(jsonify({"msg": "You are not authorised to access the page"}), 403)

        teachers = TeacherModel.query.all()
        result = list()
        result = [teacher.to_dict() for teacher in teachers]

        if len(result) > 0:
            return make_response(jsonify(result), 201)

        return make_response(jsonify({'msg': "No Result Found"}), 403)


# Resouce for getting information of particular Teacher

class ParticularTeacher(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('tid', type=str, required=True,
                        help="this field is neccesssary")

    @jwt_required
    def get(self):

        data = ParticularTeacher.parser.parse_args()

        if TeacherModel.query.filter_by(tid=data['tid']):
            teacher = TeacherModel.query.filter_by(tid=data['tid']).first()
            teacher = teacher.to_dict()

            return make_response(jsonify(teacher), 201)

        return make_response(jsonify({"msg": "Requested details not found"}), 403)


# Resource for getting teachers belonging to a particular department which receives a particular Department

class DepartmentTeacher(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument('department', type=str, required=True,
                        help='this field cannot be blank')

    def get(self):

        data = DepartmentTeacher.parser.parse_args()

        teachers = TeacherModel.query.filter_by(department=data['department'])
        result = list()
        result = [teacher.to_dict() for teacher in teachers]

        if len(result) > 0:
            return make_response(jsonify(result), 201)

        return make_response(jsonify({'msg': "No Result Found"}), 403)
