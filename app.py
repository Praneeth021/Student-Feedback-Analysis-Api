from db import db
from resources.users import Users, CurrentUser
from resources.ratings import Rating
from resources.teachers_at_classes import FindClass
from resources.Classes import Classes
from resources.teacher import Teacher, AllTeachers, DepartmentTeacher, ParticularTeacher
from resources.feedback import Feedback
from resources.login import Login
from resources.register import Register
from resources.teacher_feedback import FindTeacher
from resources.update_user import UpdateUser
from resources.update_teacher import UpdateTeacher
from resources.update_feedback import UpdateFeedback
from resources.delete_teacher import DeleteTeacher
from flask import Flask, jsonify, render_template, request, url_for, redirect, session
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from NLP_util import pred
from models.user_model import UserModel
from flask import make_response, jsonify
from sqlalchemy_serializer import SerializerMixin
import requests

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'Praneeth021'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://SQS5dSJTcg:JykCMmKcVI@remotemysql.com:3306/SQS5dSJTcg'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

jwt = JWTManager(app)
api = Api(app)

db.init_app(app)


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
api.add_resource(FindTeacher, '/t_feedback')


api.add_resource(UpdateUser, '/updateuser')
api.add_resource(UpdateTeacher, '/updateteacher')
api.add_resource(UpdateFeedback, '/updatefeedback')

api.add_resource(DeleteTeacher, '/deleteteacher')


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


@app.before_first_request
def create_database():
    db.create_all()


@app.route('/')
def Main():
    return render_template('index.html')


@app.route('/adminDashboard')
def AdminDashBoard():
    error = None
    try:
        response = requests.get('https://stufeed.herokuapp.com/dteacher',
                                data={'department': 'IT'}).json()
        response2 = requests.get('https://stufeed.herokuapp.com/ratings',
                                 headers={'Authorization': 'Bearer '+session['uid']}).json()
        data = {}
        for teacher in response:
            for t in response2:
                if(teacher['tid'] == t['teacher_id']):
                    data[teacher['tid']] = int(t['rating'])
                   

    except:
        error = 'Server Error'
    return render_template('dashboard.html', response=response, data=data)


@app.route('/AdminLogout')
def AdminLogout():
    if 'uid' in session:
        s = session.get('uid')
        del s
    return redirect(url_for('Main'))


@app.route('/adminlogin', methods=['GET', 'POST'])
def AdminLogin():
    error = None
    if request.method == 'POST':
        try:
            username = request.form.get('username')
            password = request.form.get('password')
            data = {'rollno': username, 'password': password}
            response = requests.post(
                'https://stufeed.herokuapp.com/login', data=data)
            if response.status_code != 400 or response.status_code != 500:
                session['uid'] = response.json()['access_token']
                return redirect(url_for('AdminDashBoard'))
            else:
                error = 'Invalid Credentials'
        except:
            error = 'Server Error Please try Again'
    return render_template('login.html', error=error)


if __name__ == '__main__':
    app.run(debug=True)
