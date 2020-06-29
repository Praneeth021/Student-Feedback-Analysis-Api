from flask import jsonify
from flask_restful import Resource, reqparse
from models.ratings_model import RatingModel
from models.feedback_model import FeedbackModel
from models.teachers_model import TeacherModel
from NLP_util import pred



class Rating(Resource):

    def get(self):
        teacher=TeacherModel.query.all()
        fd=list()
        for i in teacher:
            x=i.to_dict()
            fd.append(FeedbackModel.find_by_t_id(x['tid']))
            c=0
            sum=0
            for j in fd:
                feedback=j['feedback']
                r= pred(feedback)
                if(r==1):
                    sum=sum+1
                    c=c+1
                else:
                    c=c+1
                result=sum/c
                






      
