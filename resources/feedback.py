from flask import jsonify
from flask_restful import Resource, reqparse
from models.feedback_model import FeedbackModel
from flask_jwt_extended import jwt_required

from models.user_model import UserModel
from flask_jwt_extended import jwt_required,get_jwt_identity


class Feedback(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('t_id', type=str, required=True)
    parser.add_argument('feedback', type=str, required=True,
                        help="This field cannot be blank")

    @jwt_required
    def post(self):
        data = Feedback.parser.parse_args()

        current_user = get_jwt_identity()
        user=UserModel.find_by_id(id=current_user).to_dict()
        if FeedbackModel.find_by_s_id(user['rollno'], data['t_id']):
            return {"message": "You have already given"}, 400

        u = FeedbackModel(
            s_id=user['rollno'], t_id=data['t_id'], feedback=data['feedback'])
        u.save_to_db()

        return {'message': "Successfully given feedback"}, 201
