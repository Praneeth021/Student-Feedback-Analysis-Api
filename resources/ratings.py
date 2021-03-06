from flask import jsonify, make_response
from flask_restful import Resource, reqparse
from models.ratings_model import RatingModel
from models.feedback_model import FeedbackModel
from models.teachers_model import TeacherModel
from models.user_model import UserModel
from NLP_util import pred
from db import db
from flask_jwt_extended import jwt_required, get_jwt_identity


class Rating(Resource):

    @jwt_required
    def get(self):

        current_user = get_jwt_identity()

        user = UserModel.find_by_id(id=current_user).to_dict()
        if not user['admin']:
            return make_response(jsonify({"msg": "You are not authorised to view this content"}), 403)

        teachers = TeacherModel.query.all()

        for teacher in teachers:
            x = teacher.to_dict()
            rating=0
            feedbacks = FeedbackModel.find_by_t_id(t_id=x['tid'])
            if len(feedbacks) > 0:
                i = j = 0
                for feedback in feedbacks:
                    y = feedback.to_dict()
                    print(y)
                    prediction = pred(y['feedback'])
                    print(prediction)
                    if(prediction == 1):
                        j += 1
                    i += 1
                rating = j/i
                print(rating)
            if(RatingModel.find_by_id(x['tid'])):
                model = RatingModel.find_by_id(x['tid'])
                model.rating = rating
                db.session.commit()
            else:
                model = RatingModel(teacher_id=x['tid'], rating=rating)
                model.save_to_db()
        result= RatingModel.query.all()
        d=[]
        for i in result:
            i=i.to_dict()
            d.append(i)

        return make_response(jsonify(d), 200)
