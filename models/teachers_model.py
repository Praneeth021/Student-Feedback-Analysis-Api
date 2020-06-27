from db import db
from sqlalchemy_serializer import SerializerMixin

class TeacherModel(db.Model, SerializerMixin):
    __tablename__='teachers'
    tid=db.Column(db.String(30),primary_key=True)
    username=db.Column(db.String(80))
    dept=db.Column(db.String(80))
    gender=db.Column(db.String(30))
    image=db.Column(db.String(80))
    desig=db.Column(db.String(80))
    email=db.Column(db.String(80))
    date_join=db.Column(db.String(15))

    


    def __init__(self,tid,username,dept,gender,image,desig,email,date_join):
        self.tid=tid
        self.username=username
        self.dept=dept      
        self.gender=gender
        self.image=image
        self.desig=desig
        self.email=email
        self.date_join=date_join

         

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    
    @classmethod
    def find_by_tid(cls,tid):
        return cls.query.filter_by(tid=tid).first()

    