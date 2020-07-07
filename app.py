from resources.users import Users, CurrentUser
from resources.ratings import Rating
from resources.teachers_at_classes import FindClass
from resources.Classes import Classes
from resources.teacher import Teacher, AllTeachers, DepartmentTeacher, ParticularTeacher
from resources.feedback import Feedback
from resources.login import Login
from resources.register import Register
from flask import Flask, jsonify, render_template, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from NLP_util import pred
from models.user_model import UserModel
from flask import make_response, jsonify
from sqlalchemy_serializer import SerializerMixin

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'Praneeth021'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:Password@stufeed.cfwpslxqguuv.us-east-1.rds.amazonaws.com:3306/feedback'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

jwt = JWTManager(app)
api = Api(app)


# Endpoints for apis
api.add_resource(Register, '/register')
api.add_resource(Login, '/login')
api.add_resource(Users, '/users')
api.add_resource(CurrentUser, '/user/')
api.add_resource(Feedback, '/feedback')
api.add_resource(Teacher, '/teacher')  # endpoint for adding a teacher
api.add_resource(ParticularTeacher, '/pteacher')
api.add_resource(AllTeachers, '/teachers')
# endpoint for all teachers belonging to a particular department
api.add_resource(DepartmentTeacher, '/dteacher')
api.add_resource(Classes, '/class')
# endpoint for all teachers going to particular class and section in a particular department
api.add_resource(FindClass, '/findClass')
api.add_resource(Rating, '/ratings')


@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({
        'error': 'authorization_required',
        "description": "Request does not contain an access token."
    }), 401


@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({
        'error': 'invalid_token',
        'message': 'Signature verification failed.'
    }), 401





@app.route('/')
def Main():
    return "<h1>StuFeed Api Endpoints</h1>"


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    db.create_all()
    app.run()
