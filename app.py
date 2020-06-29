from flask import Flask, jsonify, render_template, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from NLP_util import pred

from models.user_model import UserModel
from flask import make_response,jsonify
from sqlalchemy_serializer import SerializerMixin

app=Flask(__name__)

app.config['JWT_SECRET_KEY']='Mahitha20'
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost:3306/feedback'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

jwt=JWTManager(app)
api=Api(app)


from resources.register import Register
from resources.login import Login
from resources.users import Users,UsersByRollno
from resources.feedback import Feedback
from resources.teacher import Teacher
from resources.Classes import Classes
from resources.teachers_at_classes import FindClass
from resources.ratings import Rating

#Endpoints for apis
api.add_resource(Register,'/register')
api.add_resource(Login,'/login')
api.add_resource(Users,'/users')
api.add_resource(UsersByRollno,'/users/<string:rollno>')
api.add_resource(Feedback,'/feedback')
api.add_resource(Teacher,'/teacher')
api.add_resource(Classes, '/class')
api.add_resource(FindClass, '/findClass')
api.add_resource(Rating,'/ratings')
    



@app.before_first_request
def create():
    db.create_all()


if __name__=='__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True)
