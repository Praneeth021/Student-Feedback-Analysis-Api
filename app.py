from flask import Flask, jsonify, render_template, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from NLP_util import pred

app=Flask(__name__)

app.config['JWT_SECRET_KEY']='praneeth021'
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost:3306/feedback'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

jwt=JWTManager(app)
api=Api(app)




from resources.register import Register
from resources.login import Login

api.add_resource(Register,'/register')
api.add_resource(Login,'/login')


@app.before_first_request
def create():
    db.create_all()


if __name__=='__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True)
