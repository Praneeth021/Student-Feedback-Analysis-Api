from db import db
from sqlalchemy_serializer import SerializerMixin

class UserModel(db.Model, SerializerMixin):
    __tablename__='users'
    rollno=db.Column(db.String(100),primary_key=True)
    username=db.Column(db.String(80))
    dept_name=db.Column(db.String(80))
    sec=db.Column(db.String(10))
    year=db.Column(db.String(10))
    password=db.Column(db.String(80))

    def __init__(self,rollno,username,password,dept_name,year,sec):
        self.username=username
        self.rollno=rollno
        self.dept_name=dept_name
        self.sec=sec
        self.year=year
        self.password=password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls,id):
        return cls.query.filter_by(rollno=id).first()


    @classmethod
    def find_by_username(cls,username):
        return cls.query.filter_by(username=username).first()


    

    