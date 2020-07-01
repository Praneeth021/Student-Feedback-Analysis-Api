from flask import jsonify
from flask_restful import Resource, reqparse
from models.feedback_model import FeedbackModel
from flask_jwt_extended import jwt_required


class Feedback(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('s_id', type=str, required=True)
    parser.add_argument('t_id', type=str, required=True)
    parser.add_argument('feedback', type=str, required=True,
                        help="This field cannot be blank")

    @jwt_required
    def post(self):
        data = Feedback.parser.parse_args()

        if FeedbackModel.find_by_s_id(data['s_id'], data['t_id']):
            return {"message": "You have already given"}, 400

        u = FeedbackModel(
            s_id=data['s_id'], t_id=data['t_id'], feedback=data['feedback'])
        u.save_to_db()

        return {'message': "Successfully given feedback"}, 201
