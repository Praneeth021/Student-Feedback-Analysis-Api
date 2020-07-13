from flask import jsonify, make_response
from flask_restful import Resource, reqparse, request
from models.feedback_model import FeedbackModel
from db import db
from flask_jwt_extended import jwt_required, get_jwt_identity

class UpdateFeedback(Resource):

    @jwt_required
    def put(self):

        current_user= get_jwt_identity()
        t_id= request.json.get('t_id')

        user = FeedbackModel.find_by_s_id(s_id=current_user, t_id=t_id)

        user.feedback=request.json.get('feedback', user.feedback)
        db.session.commit()
        return ({"msg":"updated"})
