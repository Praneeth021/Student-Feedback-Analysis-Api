from db import db
from sqlalchemy_serializer import SerializerMixin

class TeacherModel(db.Model, SerializerMixin):
    __tablename__='teachers'
    tid=db.Column(db.String(30),primary_key=True)
    username=db.Column(db.String(80))


    def __init__(self,tid,username):
        self.username=username
        self.tid=tid
        

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


    