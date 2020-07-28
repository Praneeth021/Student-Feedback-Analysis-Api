from flask import jsonify, make_response
from flask_restful import Resource, reqparse
from models.teachers_model import TeacherModel
from models.user_model import UserModel
from models.feedback_model import FeedbackModel
from models.class_model import ClassModel
from flask_jwt_extended import jwt_required, get_jwt_identity
 
class FindTeacher(Resource):

    @jwt_required
    def get(self):
        current_user=get_jwt_identity()
        user = UserModel.find_by_id(id=current_user).to_dict()
        teacher = ClassModel.find_by_class(
            user['department'], user['year'], user['section'])
        d= list()
        for i in teacher:
            x= i.to_dict()
            y=FeedbackModel.find_by_s_id(s_id=current_user, t_id=x['teacher_id'])
            if y is None:
                d.append(TeacherModel.find_by_tid(x['teacher_id']).to_dict())


        return make_response(jsonify(d), 201)

                
        
        