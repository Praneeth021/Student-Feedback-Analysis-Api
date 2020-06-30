from flask import jsonify,make_response
from flask_restful import Resource, reqparse
from models.ratings_model import RatingModel
from models.feedback_model import FeedbackModel
from models.teachers_model import TeacherModel
from NLP_util import pred
from db import db
from flask_jwt_extended import jwt_required



class Rating(Resource):

    @jwt_required
    def get(self):
        
        teachers=TeacherModel.query.all()

        for teacher in teachers:
            x=teacher.to_dict()
            print(x)
            feedbacks=FeedbackModel.find_by_t_id(t_id=x['tid'])
            i=j=0
            for feedback in feedbacks:
                y=feedback.to_dict()
                print(y)
                prediction=pred(y['feedback'])
                print(prediction)
                if(prediction==1):
                    j+=1
                i+=1
            rating=j/i
            print(rating)
            try:
                model=RatingModel.find_by_id(x['tid'])
                model.rating=rating
                db.session.commit()
            except:
                model=RatingModel(teacher_id=x['tid'],rating=rating)
                model.save_to_db()
        return make_response(model.to_dict(),200)